"""The clients model"""
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=150)
    username = models.CharField(_('username'), max_length=150, null=True)
    is_staff = models.BooleanField(
            _('staff status'),
            default=False,
            help_text=_('Designates whether the user can log '
                        'into this admin site.'),
    )
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]
