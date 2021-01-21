from django.db import models

class Banner(models.Model):
    banner_title = models.CharField(max_length=100)
    banner_dateOfEvent = models.DateField(max_length=100)
    banner_address = models.TextField()
    banner_image = models.ImageField(upload_to ='bannerImages/') 

    # tab 1 fields
    tab1_title = models.CharField(max_length=100)
    tab1_description = models.TextField()    


    # tab 2 fields Note:Category will be added here
    tab2_title = models.CharField(max_length=100)
    tab2_description = models.TextField()    

    # tab 2 fields Note:Category will be added here
    tab3_title = models.CharField(max_length=100)
    tab3_description = models.TextField()    
    tab3_venue = models.CharField(max_length=100)
    tab3_address = models.TextField()

    def __str__(self):
        return self.banner_title



class Category(models.Model):
   category_title = models.CharField(max_length=100)
   register_price = models.IntegerField()
   register_late_price = models.IntegerField()
   banner = models.ForeignKey('Banner', on_delete=models.CASCADE,related_name="Categorybanner")


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='Hotel/') 
    banner = models.ForeignKey('Banner', on_delete=models.CASCADE,related_name="Hotelbanner")


