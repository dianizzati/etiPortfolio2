from django.db import models

class Education(models.Model):
    certification = models.CharField(max_length=100)
    school = models.TextField()
    year = models.CharField(max_length=20)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
