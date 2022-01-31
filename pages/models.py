from tabnanny import verbose
from django.db import models
from courses.models import CourseList

# Create your models here.
class Homework(models.Model):
    title = models.CharField(max_length=120, verbose_name="Ödev Başlığı", blank=None, null=None)
    desc = models.TextField(verbose_name="Ödev İçeriği", blank=None, null=None)
    startdate = models.DateTimeField(verbose_name="Ödev Başlangıç Tarihi")
    enddate = models.DateTimeField(verbose_name="Ödev Bitiş Tarihi")
    
    homeworklist = models.ForeignKey(CourseList, on_delete=models.CASCADE, default="", related_name="homework_list")


class Notification(models.Model):
    notifTitle = models.CharField(max_length=120,verbose_name="Duyuru Başlığı", blank=None, null=None)
    notifDesc = models.TextField(verbose_name="Duyuru İçeriği", blank=None, null=None)
    notifDate = models.DateTimeField(verbose_name="Duyuru Yayım Tarihi", auto_now=True)

    def __str__(self):
        return self.notifTitle