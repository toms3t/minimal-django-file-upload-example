from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')

class Airplane(models.Model):
    airplane_name = models.CharField(max_length=200)
    airplane_model = models.CharField(max_length=200)
    airplane_id = models.CharField(max_length=200)
