from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField

# Create your models here.

class blogg(models.Model):
    title = TextField()
    # image = ImageField()
    text_blog = RichTextField()
