from django.db import models
from django.urls import reverse


class Uploads(models.Model):
    file_name = models.CharField(max_length=30, unique=True)
    upl_file = models.FileField(upload_to='')
    upl_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

