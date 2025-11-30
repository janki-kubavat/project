// static/script.js
document.addEventListener('DOMContentLoaded', ()=> {
  const toggle = document.getElementById('theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', () => {
      document.documentElement.classList.toggle('midnight');
      toggle.textContent = document.documentElement.classList.contains('midnight') ? 'DAY' : 'MIDNIGHT';
    });
  }

  const analyzeBtn = document.getElementById('analyze');
  if (analyzeBtn) {
    analyzeBtn.addEventListener('click', async () => {
      const tasksText = document.getElementById('tasks-json').value;
      let parsed;
      try { parsed = JSON.parse(tasksText); }
      catch (err) { alert('Invalid JSON, fix it first.'); return; }

      const strategy = document.getElementById('strategy').value;
      const resp = await fetch('/api/tasks/analyze/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tasks: parsed, strategy }),
      });
      const body = await resp.json();
      const list = document.getElementById('suggestions-list');
      list.innerHTML = '';
      if (body.results && body.results.length) {
        body.results.forEach(r => {
          const el = document.createElement('div');
          el.className = 'suggestion';
          el.innerHTML = `<div><strong>${r.title || r.id}</strong><div class="meta">${r.due_date || ''} • est: ${r.estimated_hours} • importance: ${r.importance}</div></div><div class="score">${(r.score||0).toFixed(2)}</div>`;
          list.appendChild(el);
        });
      } else {
        list.innerHTML = '<div class="empty">No suggestions returned</div>';
      }
    });
  }

  const loadExample = document.getElementById('load-example');
  if (loadExample) {
    loadExample.addEventListener('click', () => {
      document.getElementById('tasks-json').value = JSON.stringify([
        {"id":"t1","title":"Finish report","due_date":"2025-12-05","estimated_hours":3,"importance":8,"dependencies":[]},
        {"id":"t2","title":"Quick bug fix","due_date":"2025-11-30","estimated_hours":0.5,"importance":5,"dependencies":[]}
      ], null, 2);
    });
  }
});
