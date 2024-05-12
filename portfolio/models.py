from django.db import models
from django.forms import CharField, URLField
from django.db.models.fields.files import ImageField


class Projects (models.Model):
    title = CharField(max_length = 100)
    description = CharField(max_length = 250)
    image = ImageField(upload_to='media/')
