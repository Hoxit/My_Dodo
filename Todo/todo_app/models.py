from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)

class WorkToday(models.Model):

    discribe = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Date published')
    Short_discribre = models.CharField(max_length=40)
    user = models.ForeignKey(User, related_name='User', null=True)

    def __unicode__(self):
        return "{} ".format(self.Short_discribre)

