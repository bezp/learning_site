from django.db import models

# Create your models here.

class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')# blank- field isnt necessary and if nothing put in it will be default (empty str)
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Random(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)


    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title

