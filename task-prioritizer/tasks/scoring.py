from datetime import datetime
from math import exp

DEFAULT_WEIGHTS = {
    "urgency": 0.35,
    "importance": 0.35,
    "effort": 0.15,
    "dependency": 0.15,
}

STRATEGY_PRESETS = {
    "Smart Balance": DEFAULT_WEIGHTS,
    "Fastest Wins": {"urgency":0.25,"importance":0.20,"effort":0.45,"dependency":0.10},
    "High Impact": {"urgency":0.20,"importance":0.60,"effort":0.10,"dependency":0.10},
    "Deadline Driven": {"urgency":0.60,"importance":0.20,"effort":0.10,"dependency":0.10},
}

def _parse_date(s):
    try:
        return datetime.fromisoformat(s).date()
    except Exception:
        return None

def compute_score(task, all_tasks_map, weights=None, today=None):
    if today is None:
        today = datetime.utcnow().date()

    w = weights or DEFAULT_WEIGHTS

    # URGENCY
    due = _parse_date(task.get("due_date") or "")
    if due:
        days_until = (due - today).days
    else:
        days_until = 365

    if days_until < 0:
        urgency_raw = 1.0 + min(1.0, abs(days_until)/30.0)
    else:
        urgency_raw = max(0.0, 1.0 - (days_until / 30.0))

    # IMPORTANCE (1..10)
    importance_raw = (max(1, min(10, int(task.get("importance", 5)))) - 1) / 9.0

    # EFFORT (lower is better)
    est_h = task.get("estimated_hours")
    try:
        est_h = float(est_h)
        effort_raw = 1.0 / (1.0 + est_h)
    except Exception:
        effort_raw = 0.5

    # DEPENDENCY: count how many tasks this task blocks
    blocks = 0
    for t in all_tasks_map.values():
        deps = t.get("dependencies") or []
        if task.get("id") in deps:
            blocks += 1
    dependency_raw = min(1.0, blocks / 3.0)

    raw_score = (w["urgency"] * urgency_raw +
                 w["importance"] * importance_raw +
                 w["effort"] * effort_raw +
                 w["dependency"] * dependency_raw)

    final_score = round(max(0.0, min(1.0, raw_score)) * 100, 2)

    explanation = (
        f"urgency: {urgency_raw:.2f}, importance: {importance_raw:.2f}, "
        f"effort: {effort_raw:.2f}, dependency: {dependency_raw:.2f}"
    )

    return final_score, explanation

# helper: detect cycles (returns list of nodes in cycles)
def detect_cycles(tasks_map):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {tid: WHITE for tid in tasks_map}
    cycles = set()
    path = []

    def dfs(u):
        color[u] = GRAY
        path.append(u)
        for v in tasks_map[u].get("dependencies", []):
            if v not in tasks_map:
                continue
            if color[v] == WHITE:
                dfs(v)
            elif color[v] == GRAY:
                # found cycle: add nodes in cycle
                idx = path.index(v) if v in path else 0
                for node in path[idx:]:
                    cycles.add(node)
        color[u] = BLACK
        path.pop()

    for node in tasks_map:
        if color[node] == WHITE:
            dfs(node)

    return list(cycles)
