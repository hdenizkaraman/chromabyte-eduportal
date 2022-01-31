from django import template
from courses.models import CourseVideo, CourseList

register = template.Library()

@register.filter(name='nextvideo') 
def nextVideo(plist_slug, userprofile):
    userwatched = userprofile.complatedvideo.all().values_list('id', flat=True)
    allvideos = CourseVideo.objects.filter(courselist__slug=plist_slug).values_list('id', flat=True)
    lastlist =  list(set(userwatched).intersection(allvideos))
    nextvideo_id = int(lastlist[-1])+1
    getnextvideo = CourseVideo.objects.get(pk=nextvideo_id)
    return getnextvideo.videoindex
