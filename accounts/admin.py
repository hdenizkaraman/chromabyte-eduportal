from django.contrib import admin
from . models import UserProfile, Arma
# Register your models here.
@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('armatitle',)
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'schoolno','classname','place',)

