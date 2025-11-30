// auth.js - handles form submit for login/register via FormData
function getCookie(name) {
  const v = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return v ? v.pop() : '';
}

function authInit(opts) {
  const form = document.getElementById(opts.formId);
  const btn = document.getElementById(opts.submitBtnId);
  const msg = document.getElementById(opts.msgId);
  const endpoint = opts.endpoint;
  const method = opts.method || 'POST';
  const redirectOnSuccess = opts.redirectOnSuccess || '/';
  if (!form || !btn) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    msg.innerText = '';
    btn.disabled = true;
    const fd = new FormData(form);
    try {
      const res = await fetch(endpoint, {
        method,
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        body: fd,
        credentials: 'same-origin'
      });

      if (res.redirected) {
        window.location.href = res.url;
        return;
      }

      if (res.ok) {
        window.location.href = redirectOnSuccess;
        return;
      }

      // try parse JSON or text
      const ct = res.headers.get('content-type') || '';
      if (ct.includes('application/json')) {
        const data = await res.json();
        msg.innerText = data.detail || JSON.stringify(data);
      } else {
        const text = await res.text();
        msg.innerText = text || 'Error';
      }
    } catch (err) {
      console.error(err);
      msg.innerText = 'Network error — try again';
    } finally {
      btn.disabled = false;
    }
  });
}
