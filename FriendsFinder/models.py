from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Question(models.Model):
    value = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.value

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.value

class Thread(models.Model):
	title = models.CharField(max_length=128, unique=True, default='')
	slug = models.SlugField(unique=True, default='')
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Thread, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Post(models.Model):
	thread = models.ForeignKey(Thread, default='')
	title = models.CharField(max_length=128, default='')

	def __str__(self):
		return self.title	

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural = 'pages'
	
	def __str__(self): # For Python 2, use __unicode__ too
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