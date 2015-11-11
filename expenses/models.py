from django.db import models


class Expense(models.Model):
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2)
    details = models.TextField()
