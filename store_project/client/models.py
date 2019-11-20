"""The clients model"""
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('first name'), max_length=150)
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
