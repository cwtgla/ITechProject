from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class QuizQuestion(models.Model):
	value = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.value

class QuizQuestionChoice(models.Model):
	question = models.ForeignKey(QuizQuestion, null=True, default=None, on_delete=models.CASCADE)
	value = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.value

class ForumThread(models.Model):
	title = models.CharField(max_length=128, unique=True, default='')
	slug = models.SlugField(unique=True, default='')
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(ForumThread, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class ForumThreadComment(models.Model):
	thread = models.ForeignKey(ForumThread, default='')
	title = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.title	

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	# Override the __unicode__() method to return out something meaningful!
	# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username