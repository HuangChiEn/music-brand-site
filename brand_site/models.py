from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField('description', max_length=500, blank=True)
    update_at = models.DateTimeField('update time', auto_now_add=True) 
    
    class Meta:
        ordering = ('-update_at',)
    
    def __str__(self):
        return self.title

    
class VideoPost(Post):
    vdo_url = models.URLField('video url', null=True)
    video_stamp = models.TextField('video stamp', max_length=200)

class PodcastPost(Post):
    pod_url = models.URLField('podcast url', null=True)
    podcaster = models.CharField('podcaster', max_length=100)
    record_stamp = models.DateTimeField(default=datetime.now)

class ImagePost(Post):
    img_url = models.URLField('image url', null=True)
