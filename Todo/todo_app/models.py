from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
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


class InputForm(forms.Form):
    Short_discribre = forms.CharField(max_length=80)
    # email = forms.EmailField(max_length=254)
    # pub_date = models.DateTimeField('Date published')
    discribe = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!')
    source = forms.CharField(  # A hidden input for internal use
        max_length=50,  # tell from which page the user sent the message
        widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(InputForm, self).clean()
        Short_discribre = cleaned_data.get('Short_discribe')
        # email = cleaned_data.get('email')
        # pub_date = cleaned_data.get('Date published')
        message = cleaned_data.get('message')
        if not Short_discribre and not message:
            raise forms.ValidationError('You have to write something!')

    def __unicode__(self):
        return "{} ".format(self.Short_discribre)