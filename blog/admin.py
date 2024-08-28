from django.contrib import admin

from blog.models import Blog

admin.site.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'created_date', 'published', 'views_counter'),
    list_filter = ('id', 'title', 'slug', 'content', 'preview'),
    search_fields = ('title', 'slug', 'content'),