from django.contrib import admin

# Register your models here.
from .models import Course, Step
from . import models


class StepInline(admin.StackedInline):#TabulaarInline is an alt for StackedInline
    model = Step




class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline, ]

#class StepAdmin(admin.ModelAdmin):
#    inlines = [RandomInline, ]


#admin.site.register(Course, CourseAdmin)    these 3 removes after changing to the bot 6
#admin.site.register(Step)#StepAdmin  I took it out b/c im putting it under CourseAdmin
#admin.site.register(Random)

admin.site.register(models.Course)
admin.site.register(models.Text)
admin.site.register(models.Quiz)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)