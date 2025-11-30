from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .scoring import compute_score, STRATEGY_PRESETS

class ScoringTests(TestCase):
    def test_urgency_priority(self):
        today = None
        t1 = {"id":"a","title":"due yesterday","due_date":"2000-01-01","estimated_hours":1,"importance":5}
        t2 = {"id":"b","title":"due later","due_date":"2999-01-01","estimated_hours":1,"importance":5}
        tasks = {"a": t1, "b": t2}
        s1, _ = compute_score(t1, tasks, weights=STRATEGY_PRESETS["Smart Balance"])
        s2, _ = compute_score(t2, tasks, weights=STRATEGY_PRESETS["Smart Balance"])
        self.assertTrue(s1 >= s2)

    def test_effort_bias_fastest_wins(self):
        t1 = {"id":"a","title":"quick","due_date":"2999-01-01","estimated_hours":0.5,"importance":5}
        t2 = {"id":"b","title":"long","due_date":"2999-01-01","estimated_hours":8,"importance":5}
        tasks = {"a": t1, "b": t2}
        s1, _ = compute_score(t1, tasks, weights=STRATEGY_PRESETS["Fastest Wins"])
        s2, _ = compute_score(t2, tasks, weights=STRATEGY_PRESETS["Fastest Wins"])
        self.assertTrue(s1 > s2)

    def test_dependency_increases_score(self):
        t1 = {"id":"a","title":"core","due_date":"2999-01-01","estimated_hours":2,"importance":5}
        t2 = {"id":"b","title":"dep1","due_date":"2999-01-01","estimated_hours":1,"importance":3,"dependencies":["a"]}
        t3 = {"id":"c","title":"dep2","due_date":"2999-01-01","estimated_hours":1,"importance":3,"dependencies":["a"]}
        tasks = {"a": t1, "b": t2, "c": t3}
        s_core, _ = compute_score(t1, tasks)
        s_dep, _ = compute_score(t2, tasks)
        self.assertTrue(s_core >= s_dep)  # core that blocks others should be equal or higher
