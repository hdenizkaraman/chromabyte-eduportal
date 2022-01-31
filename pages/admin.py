from django.contrib import admin
from . models import Notification, Homework

# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notifTitle',)

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'startdate', 'enddate',)    