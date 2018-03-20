from django import forms
from django.contrib.auth.models import User
from FriendsFinder.models import Page, Category, UserProfile

from FriendsFinder.models import Thread, Post

class ThreadForm(forms.ModelForm):
	title = forms.CharField(max_length=128)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Thread
		fields = ('title',)

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

 # An inline class to provide additional information on the form.
	class Meta:
# Provide an association between the ModelForm and a model
		model = Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
							help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200,
						help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
# Provide an association between the ModelForm and a model
		model = Page
		exclude = ('category',)
		
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
# If url is not empty and doesn't start with 'http://',
# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
			
			return cleaned_data

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
							help_text="Please enter the title of the page.")

	class Meta:
# Provide an association between the ModelForm and a model
		model = Post
		exclude = ('thread',)
		
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
# If url is not empty and doesn't start with 'http://',
# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
			
			return cleaned_data
			
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture',)