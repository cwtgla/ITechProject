from django import forms
from django.contrib.auth.models import User
from FriendsFinder.models import UserProfile

from FriendsFinder.models import ForumThread, ForumThreadComment

class ThreadForm(forms.ModelForm):
	title = forms.CharField(max_length=128)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = ForumThread
		fields = ('title',)

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
							help_text="Please enter the title of the page.")

	class Meta:
# Provide an association between the ModelForm and a model
		model = ForumThreadComment
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