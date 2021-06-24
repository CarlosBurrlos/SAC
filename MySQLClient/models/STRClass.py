from django.db import models
from django.utils.translation import gettext_lazy as _

class STRClass(models.TextChoices):
    HATWORLD =  'HW',   _('Hatworld')
    CANADA =    'CD',   _('Canada')
    PR =        'PR',   _('PR')
    FANATICS =  'F',    _('Fanatics')
    UK =        'UK',   _('UK')
    REGULAR =   'RG',   _('Regular')
