from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class QuizQuestion(models.Model):
	questionContent = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.questionContent

class QuizQuestionChoice(models.Model):
	questionChoiceContent = models.ForeignKey(QuizQuestion, null=True, default=None, on_delete=models.CASCADE)
	questionChoiceValue = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.questionChoiceValue

class ForumThread(models.Model):
	threadTitle = models.CharField(max_length=128, unique=True, default='')
#threadCreator = models.ForeignKey(Character, blank=False)
	threadSlug = models.SlugField(unique=True, default='')
	
	def save(self, *args, **kwargs):
		self.threadSlug = slugify(self.threadTitle)
		super(ForumThread, self).save(*args, **kwargs)

	def __str__(self):
		return self.threadTitle

class ForumThreadComment(models.Model):
	linkedThread = models.ForeignKey(ForumThread, default='')
	commentContent = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.commentContent

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