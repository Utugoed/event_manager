from uuid import uuid4

from django.db import models

from organisations.models import Organisation


def event_image_path(instance, filename):
    return f"events_logos/{uuid4()}.{filename.split('.')[-1]}"

class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    organisations = models.ManyToManyField(Organisation)
    image = models.ImageField(upload_to=event_image_path)
    date = models.DateField()

    def __str__(self):
        return self.title