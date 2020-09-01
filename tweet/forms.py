from django import forms
from . import models

class AddTweetForm(forms.Form):
    text_content = forms.CharField(max_length=140, widget=forms.Textarea)
    
