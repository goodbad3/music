from django.contrib import admin
 
# Register your models here.
from django.contrib import admin
from .models import BlogArticles

admin.site.site_title = 'MyDjango后台管理123'
admin.site.site_header = 'MyDjango123'

@admin.register(BlogArticles)
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "publish")
    list_filter = ("publish", "user")
    search_fields = ("title", "body")
    raw_id_fields = ("user",)
    date_hierarchy = "publish"
    ordering = ['-publish', 'user']


