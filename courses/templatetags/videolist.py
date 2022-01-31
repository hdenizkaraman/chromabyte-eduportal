from django import template
from courses.models import CourseVideo, CourseList

register = template.Library()

@register.filter(name='times') 
def times(start, end):
    return range(int(start), int(end)+1)


@register.filter(name='videounit') 
def videoUnit(indexvalue, courselist):
    thevideo = CourseVideo.objects.filter(videoindex=int(indexvalue), courselist__title=courselist).first()
    return thevideo

@register.filter(name='videoslug') 
def videoSlug(indexvalue, courselist):
    thevideo = CourseVideo.objects.filter(videoindex=int(indexvalue), courselist__title=courselist).first()
    return thevideo.slug

@register.filter(name='watchedvideo') 
def watchedVideo(plist_slug, userprofile):
    userwatched = userprofile.complatedvideo.all()
    allvideos = CourseVideo.objects.filter(courselist__slug=plist_slug)
    lastlist =  list(set(userwatched).intersection(allvideos))
    return lastlist

@register.filter(name='turnlist')
def turnList(element):
    emptylist = []
    for x in element:
        emptylist.append(x.slug)
    return emptylist


@register.filter(name='nextvideo') 
def nextVideo(plist_slug, userprofile):
    userwatched = userprofile.complatedvideo.all().values_list('id', flat=True)
    allvideos = CourseVideo.objects.filter(courselist__slug=plist_slug).values_list('id', flat=True)
    lastlist =  list(set(userwatched).intersection(allvideos))
    nextvideo_id = int(lastlist[-1])+1
    getnextvideo = CourseVideo.objects.get(pk=nextvideo_id)
    return getnextvideo.videoindex

