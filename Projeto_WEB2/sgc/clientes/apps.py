from django.apps import AppConfig

class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # classe base do Django para configurar aplicações, BigAutoField é a definição em 64 bits
    name = 'clientes'

# define uma classe de configuração para a pagina/app "clientes", informando ao django como ele deve ser carregado e configurado
