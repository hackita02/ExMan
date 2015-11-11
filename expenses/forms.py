from django import forms
from . import models


# class ExpenseForm(forms.Form):
#     timestamp = forms.DateTimeField()
#     amount = forms.DecimalField(max_digits=12,
#                                  decimal_places=2)
#     details = forms.CharField(widget=forms.TextInput())

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = ()
