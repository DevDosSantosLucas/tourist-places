from django.contrib import admin
from .models import comment
from .actions import approve_comments, disapprove_comments

class CommentsAdmin(admin.ModelAdmin):
    list_display= ['user','date', 'approved']
    actions = [approve_comments,disapprove_comments]


admin.site.register(comment,CommentsAdmin)
