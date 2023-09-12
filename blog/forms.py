from django import	forms
from django.forms import ModelForm
from .models import Blog     # class name in models to import

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog         #class name in models
		fields = "__all__" 