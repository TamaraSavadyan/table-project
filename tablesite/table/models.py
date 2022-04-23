from django.db import models
from datetime import datetime
# Create your models here.


class TableContent(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=200, default='...')
    amount = models.IntegerField(default=0)
    distance = models.DecimalField(max_digits=20, decimal_places=3, default=0.0)

    class Meta:
        db_table = 'market_data'

    def __str__(self):
        return self.name
