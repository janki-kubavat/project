// theme.js - simple switcher
(function(){
  const linkId = 'site-theme';
  let link = document.getElementById(linkId);
  if(!link){
    link = document.createElement('link');
    link.id = linkId;
    link.rel = 'stylesheet';
    document.head.appendChild(link);
  }

  const THEMES = {
    midnight: '/static/theme-midnight.css'
  };

  // default saved or midnight
  const saved = localStorage.getItem('tp-theme') || 'midnight';
  function apply(name){
    link.href = THEMES[name] || THEMES['midnight'];
    localStorage.setItem('tp-theme', name);
  }
  apply(saved);

  // hook up theme-toggle if present (keeps API for earlier toggle)
  const btn = document.getElementById('theme-toggle');
  if(btn){
    btn.addEventListener('click', ()=>{
      const current = localStorage.getItem('tp-theme') || 'midnight';
      const next = current === 'midnight' ? 'midnight' : 'midnight';
      apply(next);
    });
  }
})();
