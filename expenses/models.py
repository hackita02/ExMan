from django.conf import settings
from django.db import models


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2)
    details = models.TextField()
