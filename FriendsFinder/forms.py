from django import forms
from django.contrib.auth.models import User
from FriendsFinder.models import UserProfile
from FriendsFinder.models import ForumThread, ForumThreadComment

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture',)

class ForumThreadForm(forms.ModelForm):
	threadTitle = forms.CharField(max_length=128)
	threadSlug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = ForumThread
		fields = ('threadTitle',)

class ForumThreadCommentForm(forms.ModelForm):
	commentContent = forms.CharField(max_length=128,help_text="Please enter the title of the page.")

	#Creating association between the form and the model its for
	class Meta:
		model = ForumThreadComment
		exclude = ('linkedThread',)