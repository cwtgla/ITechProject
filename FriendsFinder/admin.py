from django.contrib import admin
from FriendsFinder.models import Category, Page
from FriendsFinder.models import UserProfile

from FriendsFinder.models import Question, Choice
from FriendsFinder.models import Thread, Post

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Thread)
admin.site.register(Post)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
#admin.site.register(Page, PageAdmin)

class ThreadAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)	

admin.site.unregister(Thread)
admin.site.register(Thread, ThreadAdmin)
	
