from django.db import models
from datetime import datetime
from SampannaLighthouse.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length= 250, unique= True) 

    def __str__(self):
        return self.name
 


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length= 200)
    description= models.CharField(max_length=200)
    details= models.TextField()
    price = models.IntegerField()
    # slug = models.SlugField(max_length= 250, unique= True) 
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




































# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(slug_generator, sender = Cable)
# def create_slug(instance, new_slug= None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Gadget.objects.filter(slug = slug).order_by("-id")


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     slug = slugify(instance.title)

#     exists = Gadget.objects.filter(slug = slug).exists()
#     if exists:
#         slug = "%s-%s" %(slug, instance.id)

#     instance.slug = slug


# pre_save.connect(pre_save_post_receiver, sender = Gadget)