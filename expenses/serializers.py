from rest_framework import serializers
from . import models


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = (
            'id',
            'user',
            'timestamp',
            'amount',
            'details',
        )
