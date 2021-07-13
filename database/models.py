from django.db.models import *
from django.db import *

# Create your models here.
class Text(Model):
    name = TextField()