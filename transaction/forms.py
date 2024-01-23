from django import forms
from .models import TransactionModel

class DepositForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount']

    