from django import forms
from .models import Calculation, Number, Operation

class CalculationForm(forms.ModelForm):
    left_operand = forms.ModelChoiceField(queryset=Number.objects.all())
    operation = forms.ModelChoiceField(queryset=Operation.objects.all())
    right_operand = forms.ModelChoiceField(queryset=Number.objects.all())
    
    class Meta:
        model = Calculation
        fields = ('left_operand', 'operation', 'right_operand',)
