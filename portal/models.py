from __future__ import unicode_literals
import string
import random
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Category, self).save(*args, **kwargs)


class UserRole(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Category, self).save(*args, **kwargs)



class Status(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Status, self).save(*args, **kwargs)



class UserProfile(models.Model):
    user = models.ForeignKey(User)
    contact = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    user_role = models.ForeignKey(UserRole)
    registered_by = models.CharField(max_length=255)
    registered_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status)


class Analytic(models.Model):
    code = models.CharField(max_length=6)
    action = models.CharField(max_length=255)
    description = models.TextField()
    ip_address = models.CharField(max_length=255)
    gps_location = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Analytic, self).save(*args, **kwargs)


class DataSet(models.Model):
    specie_code = models.CharField(max_length=6)
    scientific_name = models.CharField(max_length=255)
    local_name = models.CharField(max_length=255)
    scientific_pronounciation = models.FileField(upload_to="pronounciation/")
    local_pronounciation = models.FileField(upload_to="pronounciation/")
    gps = models.CharField(max_length=20)
    address = models.TextField()
    version = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="specie.png", upload_to="specie_images/")
    description = models.TextField()
    reviewer_1 = models.CharField(max_length=255)
    reviewer_2 = models.CharField(max_length=255)
    status = models.ForeignKey(Status)
    reviewer_1_date = models.DateTimeField(null=True)
    reviewer_2_date = models.DateTimeField(null=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.specie_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(DataSet, self).save(*args, **kwargs)


class Comment(models.Model):
    specie = models.ForeignKey(DataSet)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=255)
    status = models.ForeignKey(Status)
    gps_location = models.CharField(max_length=255)
