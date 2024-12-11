from django import forms
from .models import FinancialEntry

class FinancialEntryForm(forms.ModelForm):
    class Meta:
        model = FinancialEntry
        fields = ['item', 'amount']

