from django.contrib import admin

# Register your models here.
from .models import Course, Step, Random


class StepInline(admin.StackedInline):
    model = Step

class RandomInline(admin.StackedInline): #TabulaarInline is an alt for StackedInline
    model = Random


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline, RandomInline, ]

#class StepAdmin(admin.ModelAdmin):
#    inlines = [RandomInline, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Step)#StepAdmin  I took it out b/c im putting it under CourseAdmin
admin.site.register(Random)