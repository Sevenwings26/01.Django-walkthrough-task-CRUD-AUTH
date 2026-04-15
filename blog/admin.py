from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from . import models

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(models.BlogPost, SomeModelAdmin)

# Register your models here.
admin.site.register(models.BlogPostCategory)
admin.site.register(models.AuthourProfile)


# admin.site.register(models.BlogPost)
# @admin.register(models.BlogPost)
# class BlogAdminSite(admin.ModelAdmin):
#     list_display = ('title', 'author')

