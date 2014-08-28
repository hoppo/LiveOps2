from django.db import models

class Match(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bt = models.BooleanField()
    adi = models.BooleanField()
    isdn = models.CharField(max_length=12, unique=True)
    sound_eng = models.CharField(max_length=12)
    gallery = models.IntegerField()

    def __unicode__(self):
        return self.name
