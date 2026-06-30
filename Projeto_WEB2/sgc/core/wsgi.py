import os # módulo para manipular variáveis
from django.core.wsgi import get_wsgi_application # wsgi define como um servidor web Python deve se comunicar com uma aplicação web (como o Django aqui).

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') # Define qual arquivo de configurações o djago vai usar, no caso aqui, é o "settings.py"
application = get_wsgi_application() # Cria a instância da aplicação WSGI
