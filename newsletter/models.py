from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField(max_length='200', blank=False)
    full_name = models.CharField(max_length='200', blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return self.email