from email.policy import default
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class CourseList(models.Model):
    title = models.CharField(max_length=120, verbose_name="Kurs Listesi İsmi", default="Yeni Kurs Listesi")
    desc = models.TextField(verbose_name="Eğitim Seti Açıklaması", default="Açıklama Eklenmemiştir!")
    banner = models.ImageField(verbose_name="Kurs Kapağını Yükleyiniz", upload_to="courselists/", default="courselists/wp1.jpg")
    slug = models.SlugField(max_length=200, unique=True, null=True)


    def __str__(self):
        return self.title

class CourseUnits(models.Model):
    nameUnit = models.CharField(max_length=160, verbose_name="Bölüm Adı", default="Yeni Ünite")
    playlist = models.ForeignKey(CourseList, on_delete=models.CASCADE, default="", related_name="plist_units")
    videoindex_start = models.PositiveIntegerField(null=True)
    videoindex_end = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.nameUnit

class CourseVideo(models.Model):  
    name = models.CharField(max_length=180, verbose_name="Video İsmi", default="Adlandırılmamış Video")
    slug = models.SlugField(max_length=200, unique=True, null=True)
    desc = models.TextField(verbose_name="Ders Açıklaması", default="Bu Ders İçin Açıklamaya Gerek Yoktur!")
    attach = models.URLField(verbose_name="İlgili Dosya Linki", default="", blank=True, null=True)
    driveid = models.CharField(max_length= 200, verbose_name="Video Drive Id", default="0000x")
    videoindex = models.IntegerField(verbose_name="Oynatma Listesi Index Sırası", default=999)

    courselist = models.ForeignKey(CourseList, on_delete=models.CASCADE, default="", related_name="video_plist")
    # courseunit = models.ForeignKey(CourseUnits, on_delete=models.CASCADE, default="", null=True, related_name="video_unit")

    def __str__(self):
        return self.name

    