from django.db import models

# Create your models here.
# models.py
class Image(models.Model):
	name = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='images/')

