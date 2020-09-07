from django.db import models
from datetime import datetime


class Cable(models.Model):

    title = models.CharField(max_length= 200)
    description= models.CharField(max_length=200)
    details= models.TextField()
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    is_published = models.BooleanField(default=True)
    is_topselling = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Switch(models.Model):

    title = models.CharField(max_length= 200)
    description= models.CharField(max_length=200)
    details= models.TextField()
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    is_published = models.BooleanField(default=True)
    is_topselling = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Light(models.Model):

    title = models.CharField(max_length= 200)
    description= models.CharField(max_length=200)
    details= models.TextField()
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    is_published = models.BooleanField(default=True)
    is_topselling = models.BooleanField(default=False)


    def __str__(self):
        return self.title