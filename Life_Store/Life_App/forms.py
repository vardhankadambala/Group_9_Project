from .models import details
from django import forms

class detaisform(forms.ModelForm):
	class Meta:
		model=details
		fields="__all__"