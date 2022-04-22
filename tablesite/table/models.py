from django.db import models
from django.forms import CharField, DateTimeField, IntegerField
from psycopg2 import Timestamp

# Create your models here.

class TableContent(models.Model):
    id = IntegerField()
    date = DateTimeField()
    name = CharField(max_length=200)
    amount = IntegerField()
    distance = IntegerField()