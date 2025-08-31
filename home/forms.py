from django import forms
from .models import Feedback
from .models import Contact

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']