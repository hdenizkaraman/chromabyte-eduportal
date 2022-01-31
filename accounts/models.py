from django.db import models
from django.contrib.auth.models import User
from courses.models import CourseList, CourseVideo
# Create your models here.
class Arma(models.Model):
    armatitle = models.CharField(max_length=120, verbose_name="Arma Başlığı", default="Arma Başlığı")
    armaimage = models.ImageField(upload_to="armaimage/", default="armaimage/sirdenq.png")

    def __str__(self):
        return self.armatitle

class UserProfile(models.Model):
    name_surname = models.CharField(max_length=120, verbose_name="İsim ve Soyisim", default="AD SOYAD")
    unitname = models.CharField(max_length=60, verbose_name="Bulunulan Birim", default="BİRİM İSMİ")
    pfp = models.ImageField(upload_to="userpfp/", default="userpfp/frzallogo.png")
    classname = models.CharField(max_length=50, verbose_name="Okul Sınıfı")
    schoolno = models.IntegerField(verbose_name="Okul Numarası")
    birthday = models.DateField(verbose_name="Doğum Tarihi")
    place = models.CharField(max_length=120, verbose_name="Yaşadığı Anlık Yer")
    allergy = models.CharField(max_length=120, verbose_name="Alerji Durumu")
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="accprofile")
    arma = models.ManyToManyField(Arma, blank=True)
    lecturelist = models.ManyToManyField(CourseList, blank=True)
    complatedvideo = models.ManyToManyField(CourseVideo, blank=True)

    def __str__(self):
        return self.name_surname

