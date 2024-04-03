from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'trainee_validations'
    verbose_name = 'Trainee + Form Validations'
