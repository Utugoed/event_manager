import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from organisations.models import Organisation
from users.managers import CustomUserManager


def phone_validator(phone: str):
    if not (re.fullmatch(r"[+]79\d{9}", phone) or re.fullmatch(r"89\d{9}", phone)):
        raise ValidationError(
            gettext_lazy("%(value) is not a valide phone number"),
            params={"value": phone}
        )

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy("email_address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=12, validators=[phone_validator], null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["organisation"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    