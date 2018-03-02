from django.db import models


class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class Note(models.Model):
    description = models.TextField()
    patient = models.ForeignKey(Patient)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.description





