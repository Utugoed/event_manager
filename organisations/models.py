import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy


def validate_postcode(postcode: str):
    if not re.fullmatch(r"\d{6}", postcode):
        raise ValidationError(
            gettext_lazy('%(value)s is not a valid postcode'),
            params={"value": postcode}
        )

class Organisation(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    address = models.TextField()
    postcode = models.CharField(max_length=6, validators=[validate_postcode])

    def __str__(self):
        return self.title