from django.contrib import admin
from FriendsFinder.models import UserProfile
from FriendsFinder.models import *

admin.site.register(UserProfile)
admin.site.register(QuizQuestion)
admin.site.register(QuizQuestionChoice)
admin.site.register(ForumThread)
admin.site.register(ForumThreadComment)
admin.site.register(Character)

class ForumThreadAdmin(admin.ModelAdmin):
	prepopulated_fields = {'threadSlug':('threadTitle',)}

# Update the registration to include this customised interface
admin.site.unregister(ForumThread)
admin.site.register(ForumThread, ForumThreadAdmin)