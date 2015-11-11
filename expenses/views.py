from authtools.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from expenses import serializers
from . import models


class HomeView(LoginRequiredMixin, ListView):
    model = models.Expense

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def total(self):
        qs = self.get_queryset()
        return sum(x.amount for x in qs)


class AddView(LoginRequiredMixin, CreateView):
    model = models.Expense
    fields = (
        'timestamp',
        'amount',
        'details',
    )
    success_url = reverse_lazy("home")

    def get_initial(self):
        d = super().get_initial()
        d['timestamp'] = timezone.now()
        return d

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

    @list_route()
    def total(self, request):
        qs = self.get_queryset()
        total = sum(x.amount for x in qs)
        return Response({'total': total})
