from django.shortcuts import render
from django.http import HttpResponse
from brand_site.models import VideoPost, PodcastPost

def index_page(req):
    # prepare video info, (put early video at the head)
    vdo_lst = VideoPost.objects.all().order_by('update_at')
    tm_stamp = []
    for vdo in vdo_lst:
        tm_stamp.append( str(vdo.video_stamp).splitlines() )

    # prepare podcast info (put last video at the head)
    pod_lst = PodcastPost.objects.all().order_by('-record_stamp')

    # wrap into dict
    rend_dict = {
        'vdo_info' : zip(vdo_lst, tm_stamp),
        'pod_info' : pod_lst
    }
    return render(req, 'index.html', rend_dict)

def about_page(req):
    return render(req, 'about.html')
