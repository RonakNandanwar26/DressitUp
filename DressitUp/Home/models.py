from django.db import models
import random
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product



GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(default='')

    def __str__(self):
        return self.name

# class Add_Product(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     slug = models.SlugField()
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     quantity = models.IntegerField(default=1)
#     mfg_date = models.DateField()
#     image = models.ImageField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


#
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splittext(base_name)
    return ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,1000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "users/{final_filename}".format(final_filename=final_filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=30, null=True, blank= True)
    last_name = models.TextField(max_length=30, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    tel = models.CharField(max_length=15)     #validators should be a list
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(default=3, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    file = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        get_latest_by = "join_date"
        ordering = ['user']
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



























