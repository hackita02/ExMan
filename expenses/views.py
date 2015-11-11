from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from . import models, forms


class HomeView(ListView):
    model = models.Expense

    def total(self):
        qs = self.get_queryset()
        return sum(x.amount for x in qs)


class AddView(CreateView):
    model = models.Expense
    fields = (
        'timestamp',
        'amount',
        'details',
    )
    success_url = reverse_lazy("home")

    # form_class = forms.ExpenseForm


#
# def add(request):
#     if request.method == "POST":
#         form = forms.ExpenseForm(request.POST)
#         if form.is_valid():
#             o = form.save()
#             return redirect("home")
#     else:
#         form = forms.ExpenseForm()
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })
