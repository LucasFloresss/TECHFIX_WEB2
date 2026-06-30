const API = {
  getToken() {
    return localStorage.getItem('token');
  },

  setToken(token) {
    localStorage.setItem('token', token);
  },

  getUser() {
    try { return JSON.parse(localStorage.getItem('user')); } catch { return null; }
  },

  setUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
  },

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login/';
  },

  async request(method, url, body = null) {
    const token = this.getToken();
    if (!token) { this.logout(); return; }

    const opts = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
    };
    if (body) opts.body = JSON.stringify(body);

    const resp = await fetch(url, opts);

    if (resp.status === 401) { this.logout(); return; }

    if (!resp.ok) {
      const err = await resp.json().catch(() => ({}));
      throw err;
    }

    if (resp.status === 204) return null;
    return resp.json();
  },

  get(url) { return this.request('GET', url); },
  post(url, body) { return this.request('POST', url, body); },
  put(url, body) { return this.request('PUT', url, body); },
  patch(url, body) { return this.request('PATCH', url, body); },
  delete(url) { return this.request('DELETE', url); },
};

function mostrarErro(msg, containerId = 'alerta') {
  const el = document.getElementById(containerId);
  if (el) {
    el.innerHTML = `<div class="alerta alerta-erro">${msg}</div>`;
  }
}

function mostrarSucesso(msg, containerId = 'alerta') {
  const el = document.getElementById(containerId);
  if (el) {
    el.innerHTML = `<div class="alerta alerta-sucesso">${msg}</div>`;
  }
}

function limparAlerta(containerId = 'alerta') {
  const el = document.getElementById(containerId);
  if (el) el.innerHTML = '';
}

function formatarMoeda(valor) {
  return parseFloat(valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
}

function formatarCpf(cpf) {
  if (!cpf) return '';

  const digitos = String(cpf).replace(/\D/g, '').slice(0, 11);
  if (!digitos) return '';

  const partes = digitos.match(/.{1,3}/g) || [];
  if (partes.length <= 2) {
    return partes.join('.');
  }

  const bloco1 = partes[0] || '';
  const bloco2 = partes[1] || '';
  const bloco3 = partes[2] || '';
  const digito = partes[3] || '';

  if (digito) {
    return `${bloco1}.${bloco2}.${bloco3}-${digito}`;
  }

  return `${bloco1}.${bloco2}.${bloco3}`;
}

function mascararCpf(input) {
  const valor = String(input.value || '').replace(/\D/g, '').slice(0, 11);
  let formatado = '';

  if (valor.length > 9) {
    formatado = `${valor.slice(0, 3)}.${valor.slice(3, 6)}.${valor.slice(6, 9)}-${valor.slice(9)}`;
  } else if (valor.length > 6) {
    formatado = `${valor.slice(0, 3)}.${valor.slice(3, 6)}.${valor.slice(6)}`;
  } else if (valor.length > 3) {
    formatado = `${valor.slice(0, 3)}.${valor.slice(3)}`;
  } else {
    formatado = valor;
  }

  input.value = formatado;
}

function formatarData(iso) {
  if (!iso) return '-';
  const d = new Date(iso);
  return d.toLocaleDateString('pt-BR') + ' ' + d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
}

// Redirecionar para login se não tiver token (exceto na página de login)
document.addEventListener('DOMContentLoaded', () => {
  const naLogin = window.location.pathname === '/login/';
  if (!naLogin && !API.getToken()) {
    window.location.href = '/login/';
  }

  // Mostrar nome do usuário na sidebar
  const user = API.getUser();
  const userEl = document.getElementById('nome-usuario');
  if (userEl && user) userEl.textContent = user.username || 'Usuário';

  // Marcar link ativo
  const links = document.querySelectorAll('#sidebar nav a');
  links.forEach(link => {
    if (link.href && window.location.pathname.startsWith(new URL(link.href).pathname)) {
      link.classList.add('ativo');
    }
  });
});
