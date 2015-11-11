from authtools.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
