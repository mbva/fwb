from __future__ import unicode_literals
import string
import random
from django.db import models
from django.contrib.auth.models import User



class Insititution(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Insititution, self).save(*args, **kwargs)


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state_pronvice = models.CharField(max_length=255)
    continent = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WaterBody(models.Model):
   name = models.CharField(max_length=255)
   district = models.ForeignKey(District)

   def __str__(self):
       return self.name


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
        return self.action

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Analytic, self).save(*args, **kwargs)


class Genus(models.Model):
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255)
    genus_class = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    family = models.CharField(max_length=255)

    def __str__(self):
        return self.phylum


class Specie(models.Model):
    code = models.CharField(max_length=6)
    kingdom = models.CharField(max_length=255)
    specie_class = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    genus = models.ForeignKey(Genus)
    sub_genus = models.CharField(max_length=255)
    english_fish_base_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    specific_epithet = models.CharField(max_length=255)
    scientific_name_authorship = models.CharField(max_length=255)
    chironym = models.CharField(max_length=255)
    infraspecific_epithet = models.CharField(max_length=255)

    def __str__(self):
        return self.scientific_name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Specie, self).save(*args, **kwargs)



class DataSet(models.Model):
    name = models.CharField(max_length=255)
    narration = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    specie = models.ForeignKey(DataSet)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=255)
    status = models.ForeignKey(Status)
    gps_location = models.CharField(max_length=255)

    def __str__(self):
        return self.comment


class Occurrance(models.Model):
    code = models.CharField(max_length=6)
    data_set = models.ForeignKey(DataSet)
    specie = models.ForeignKey(Specie)
    water_body = models.ForeignKey(WaterBody)
    type_status = models.ForeignKey(Status)
    identified_by = models.ForeignKey(User)
    comments_coments = models.ForeignKey(Comment)
    originality = models.CharField(max_length=255)
    basis_of_record = models.CharField(max_length=255)
    existance = models.CharField(max_length=255)
    recorded_by = models.ForeignKey(UserProfile)
    collection_code = models.CharField(max_length=255)
    field_number = models.CharField(max_length=255)
    event_remark = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    specie_invasion = models.CharField(max_length=255)
    catalogue_number = models.CharField(max_length=255)
    sampling_protocol = models.CharField(max_length=255)
    date_identified = models.DateTimeField()
    type_locality = models.CharField(max_length=255)
    verbal_latitude = models.CharField(max_length=255)
    verbal_longitude = models.CharField(max_length=255)
    decimal_latitude = models.CharField(max_length=255)
    decimal_longitude = models.CharField(max_length=255)
    cordinate_precision = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    threat_level_fishing = models.CharField(max_length=255)
    eutrophication_and_pollution = models.CharField(max_length=255)
    habitat_modification = models.CharField(max_length=255)
    minimum_elevetion_in_meters = models.CharField(max_length=255)
    maximum_elevation_in_meters = models.CharField(max_length=255)
    threat_level_climate_change = models.CharField(max_length=255)
    invasivespecies = models.CharField(max_length=255)
    minimum_depth_in_meters = models.CharField(max_length=255)
    maximum_depth_in_meters = models.CharField(max_length=255)
    local_pronunciation = models.CharField(max_length=255)
    local_name = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.local_name

    def save(self, *args, **kwargs):
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super(Occurrance, self).save(*args, **kwargs)
