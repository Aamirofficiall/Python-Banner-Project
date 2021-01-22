from django.db import models
from ckeditor.fields import RichTextField
import datetime


class Conference(models.Model):
    title = models.CharField(max_length=100)
    detail_title = models.CharField(max_length=100)
    conference_date = models.DateField(  default=datetime.date.today, blank=True)
    address = models.CharField(max_length=255)
    venue = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = RichTextField(default='') 
    registration = RichTextField(default='') 
    image = models.ImageField(upload_to ='bannerImages/') 


    def __str__(self):
        return self.title



class Hotel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='Hotel/') 
    redirect_url = models.URLField(max_length = 200) 
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE,related_name="conferenceHotel")


