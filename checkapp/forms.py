from django import forms
from django.db.models import fields
from .models import Customers

class CustomerForm(forms.ModelForm):
  last_scanned = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Customers
    fields = "__all__"