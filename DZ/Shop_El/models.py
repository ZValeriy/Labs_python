from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfileManager(models.Manager):
    def getName(self, user_name):
        return self.filter(user__username=user_name)

    def getUsername(self, id):
        return self.filter(user__id=id)


class Brand(models.Model):
    namebrand = models.CharField(max_length=30)

    def __str__(self):
        return self.namebrand


class Product(models.Model):
    nameproduct = models.CharField(max_length=30)
    processor = models.TextField(max_length=30)
    screen_size = models.TextField(max_length=30)
    gpu = models.TextField(max_length=20)
    memory = models.TextField(max_length=30)
    description = models.TextField(max_length=1000)
    cost = models.IntegerField()
    brand = models.ForeignKey(Brand)
    img = models.ImageField(upload_to='media')
    comps = models.ManyToManyField(User)

    def get_username(self):
        count = self.comps.count()
        if count == 0:
            return 0
        else:
            return count


    def __str__(self):
        return self.nameproduct


class ProductManger(models.Manager):
    def add_or_update(self, user):
        new = self.update_or_create(comps=user)
        return new





