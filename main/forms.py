from django import forms

from main.models import ContactForm, FeaturedForm


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']

class FeaturedFormModelForm(forms.ModelForm):
    class Meta:
        model = FeaturedForm
        fields = ['name', 'email', 'sname', 'slocation', 'sdesc']