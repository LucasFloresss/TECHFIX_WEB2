// Este JavaScript é o "cérebro" do frontend, gerenciando autenticação, comunicação com a API e funções auxiliares

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
    localStorage.setItem('user', JSON.stringify(user)); // Armazena token e dados do usuário
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

function mostrarErro(msg, containerId = 'alerta') { // Feedback ruim
  const el = document.getElementById(containerId);
  if (el) {
    el.innerHTML = `<div class="alerta alerta-erro">${msg}</div>`;
  }
}

function mostrarSucesso(msg, containerId = 'alerta') { // Feedback bao
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
