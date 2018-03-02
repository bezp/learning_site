from django.contrib import admin

# Register your models here.
from . models import Patient, Note

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    inlines = [NoteInline, ]

admin.site.register(Patient, PatientAdmin)



