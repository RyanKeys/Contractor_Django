from django import forms
from .models import Listing

class AddItem(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        