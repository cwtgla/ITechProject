from django.contrib import admin
from FriendsFinder.models import UserProfile

from FriendsFinder.models import QuizQuestion, QuizQuestionChoice
from FriendsFinder.models import ForumThread, ForumThreadComment

admin.site.register(UserProfile)
admin.site.register(QuizQuestion)
admin.site.register(QuizQuestionChoice)
admin.site.register(ForumThread)
admin.site.register(ForumThreadComment)


class ThreadAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

# Update the registration to include this customised interface
admin.site.unregister(ForumThread)
admin.site.register(ForumThread, ThreadAdmin)
	
