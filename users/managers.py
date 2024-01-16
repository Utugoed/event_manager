from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy

from organisations.models import Organisation

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, organisation, **extra_fields):
        if not (email):
            raise ValueError(gettext_lazy("The Email must be set"))
        email = self.normalize_email(email)

        organisation_obj = Organisation.objects.get(id=organisation)
        
        user = self.model(email=email, organisation=organisation_obj, **extra_fields)
        user.set_password(password if extra_fields["is_superuser"] else make_password(password))
        user.save()
        return user

    def create_superuser(self, email, password, organisation, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if (extra_fields.get("is_staff") is not True):
            raise ValueError(gettext_lazy("Superuser must have is_staff=True."))
        if (extra_fields.get("is_superuser") is not True):
            raise ValueError(gettext_lazy("Superuser must have is_superuser=True."))

        return self.create_user(email, password, organisation, **extra_fields)
