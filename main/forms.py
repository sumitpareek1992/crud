from django import forms
from .models import Emp

class EmpForm(forms.ModelForm):
	dob = forms.DateField(input_formats=['%d-%m-%Y'])
	class Meta:
		model = Emp
		fields ='__all__'