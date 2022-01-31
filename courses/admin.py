from django.contrib import admin
from . models import CourseList, CourseVideo, CourseUnits
# Register your models here.
class CourseUnitsInline(admin.TabularInline):
    model = CourseUnits

@admin.register(CourseList)
class CourseListAdmin(admin.ModelAdmin):
    list_display = ["title",]
    prepopulated_fields = {"slug":('title',)}
    inlines = [
        CourseUnitsInline,
    ]

@admin.register(CourseVideo)
class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ["name", "driveid",]
    prepopulated_fields = {"slug":('name',)}
