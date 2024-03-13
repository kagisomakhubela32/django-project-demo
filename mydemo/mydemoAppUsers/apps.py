from django.apps import AppConfig


class MydemoappusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mydemoAppUsers'

    def ready(self):
        import mydemoAppUsers.signals