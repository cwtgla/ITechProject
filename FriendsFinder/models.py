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

#A Character instance exists for each User after they complete the quiz
class Character(models.Model):
	characterName = models.CharField(max_length=50, unique=True, blank=False)
	linkedUser = models.ForeignKey(User, null=True, blank=False)
	#TODO keep track of Characters created threads and comments, so admin would show name, thread,comments,datecreated,email

	#Save overwritten so that a unique number is assigned to the end of the name so you can tel between different users
	def save(self, *args, **kwargs):
		existingCount = Character.objects.filter(characterName__startswith=self.characterName).count()
		self.characterName = self.characterName + str(existingCount)
		super(Character, self).save(*args, **kwargs)

	def __str__(self):
		return self.characterName #Hack for now, idea is query how many XXXX exist and append count+1

#Model for a thread within the forum which contains standard information as well as extra like creator, modified times
class ForumThread(models.Model):
	threadTitle = models.CharField(max_length=128, unique=True, default='')
	threadCreator = models.ForeignKey(Character, blank=False,default='')
	threadContent = models.CharField(max_length=500, blank=False, default='')
	threadCreationDate = models.DateField(auto_now_add=True)
	threadLastModified = models.DateField(auto_now=True)
	threadSlug = models.SlugField(unique=True, default='')
	
	def save(self, *args, **kwargs):
		self.threadSlug = slugify(self.threadTitle)
		super(ForumThread, self).save(*args, **kwargs)

	def __str__(self):
		return self.threadTitle

class ForumThreadComment(models.Model):
	linkedThread = models.ForeignKey(ForumThread, default='')
	commentContent = models.CharField(max_length=128, blank=False)
	threadCommentCreator = models.ForeignKey(Character, blank=False,default='')
	threadCommentCreationDate = models.DateField(auto_now_add=True)
	threadCommentLastModified= models.DateField(auto_now=True)

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