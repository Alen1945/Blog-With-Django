from django import forms
from .models import Post


class CreateForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','content']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['title'].widget.attrs={'class':'form-control'}
		self.fields['content'].widget.attrs={'class':'form-control','rows':10}