from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    # List of fields that should use the Summernote editor
    summernote_fields = ('body',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
