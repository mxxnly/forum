from django import forms
from .models import YourModel

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['email', 'title', 'text', 'file']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }