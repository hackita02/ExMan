from django.shortcuts import render
from django.views.generic import ListView

from . import models


class HomeView(ListView):
    model = models.Expense

    def total(self):
        qs = self.get_queryset()
        return sum(x.amount for x in qs)
