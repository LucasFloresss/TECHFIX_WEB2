import os
import django

#  cria usuários iniciais no sistema para facilitar o desenvolvimento e teste da aplicação
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
# Cria superusuário admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@techfix.com', 'admin123')
    print("Usuário 'admin' criado com senha 'admin123'")
else:
    print("Usuário 'admin' já existe.")

# Cria usuário comum
if not User.objects.filter(username='funcionario').exists():
    u = User.objects.create_user('funcionario', 'func@techfix.com', 'func123')
    print("Usuário 'funcionario' criado com senha 'func123'")
else:
    print("Usuário 'funcionario' já existe.")
