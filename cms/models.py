from django.db import models
from django.utils.safestring import mark_safe

class Service(models.Model):
    iconImage=models.ImageField(upload_to="static/images")
    serviceTitle=models.CharField(max_length=255)
    serviceDesc=models.TextField()

    def admin_photo(self):
        return mark_safe('<img src="{}"width="80" height="80"/>'.format(self.iconImage.url))

class About(models.Model):
    aImage=models.ImageField(upload_to="static/images")
    aTitle=models.CharField(max_length=255)
    aDesc=models.TextField()

    def about_photo(self):
        return mark_safe('<img src="{}"width="80" height="80"/>'.format(self.aImage.url))


class Guard(models.Model):
    guardImage=models.ImageField(upload_to="static/images")
    guardTitle=models.CharField(max_length=255)
    guardDesc=models.TextField()

    def guard_photo(self):
        return mark_safe('<img src="{}"width="80" height="80"/>'.format(self.guardImage.url))

class Contact(models.Model):
    cname=models.CharField(max_length=255)
    cemail=models.CharField(max_length=255)
    cphone=models.CharField(max_length=10)
    cmsg=models.TextField()
    

class Registration(models.Model):
    rname=models.CharField(max_length=255)
    runame=models.CharField(max_length=255)
    remail=models.CharField(max_length=255)
    rpass=models.CharField(max_length=100)
    
    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="80" height="80" />'.format(self.iconImage.url))

    
# class contact(models.Model):
#     fname = models.CharField(max_length= 30)
#     email = models.EmailField()
#     phone = models.CharField(max_length=10)
#     msg = models.TextField()
# Create your models here.
