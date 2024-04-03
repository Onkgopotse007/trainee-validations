from django.conf import settings

if settings.APP_NAME == 'trainee_validations':
    from .tests import models