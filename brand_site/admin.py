from django.contrib import admin
from .models import VideoPost, PodcastPost, ImagePost

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'update_at']

# Register your models here.
admin.site.register(VideoPost, PostAdmin)
admin.site.register(PodcastPost, PostAdmin)
admin.site.register(ImagePost, PostAdmin)