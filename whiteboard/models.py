from django.db import models

class Match(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    bt = models.BooleanField(blank=True)
    adi = models.BooleanField(blank=True)
    gal = models.BooleanField(blank=True)
    mars = models.BooleanField(blank=True)
    swif = models.BooleanField(blank=True)
    dialled = models.BooleanField(blank=True)
    isdn = models.CharField(max_length=12,null=True,blank=True)
    codec = models.CharField(max_length=3,null=True,blank=True)
    sound_eng = models.CharField(max_length=12,null=True,blank=True)
    gallery = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.name
