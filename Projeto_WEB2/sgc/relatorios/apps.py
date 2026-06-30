from django.apps import AppConfig
# registra o app/pagina de relatorios no Django e define seu nome e configuração de ID
class RelatoriosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relatorios'
