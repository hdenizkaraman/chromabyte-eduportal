from django.shortcuts import redirect, render
from . models import CourseList, CourseUnits, CourseVideo 
from pages.models import Homework

# Create your views here.
def dersler(request):
    playlist = CourseList.objects.all()
    video = CourseVideo.objects.all()
    homework = Homework.objects.all()
    context = {
        "playlist":playlist,
        "video":video,
        "homework":homework,
    }
    return render(request, "dersler.html", context)



def egitimvideo(request, listslug, videoindex):
    try:
        playlist = CourseList.objects.get(slug=listslug)
        video = CourseVideo.objects.get(videoindex=int(videoindex))
        context = {
            "playlist":playlist, 
            "video":video,
        }
        return render(request, "egitimseti.html", context)
    except:
        return redirect("error")


def videobitir(request, videoslug):
    thevideo = CourseVideo.objects.filter(slug=videoslug)
    current_user = request.user
    idQuery = thevideo.values_list('pk', flat=True)
    query_to_list = [str(integer) for integer in list(idQuery)]
    string_id = "".join(query_to_list)
    integer_id = int(string_id)
    current_user.accprofile.complatedvideo.add(integer_id)
    return redirect("dersler")

def dersal(request, listslug):
    thelist = CourseList.objects.filter(slug=listslug)
    current_user = request.user
    idQuery = thelist.values_list('pk', flat=True)
    query_to_list = [str(integer) for integer in list(idQuery)]
    string_id = "".join(query_to_list)
    integer_id = int(string_id)
    current_user.accprofile.lecturelist.add(integer_id)
    return redirect("dersler")
