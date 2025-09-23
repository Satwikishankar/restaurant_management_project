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
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or len(message.strip()) <10:
            raise forms.ValidationError("Message must be atleast 10 characters long.")
        return message