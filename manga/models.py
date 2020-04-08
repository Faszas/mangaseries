from django.db import models
from django.utils import timezone
# Create your models here.

class myManga(models.Model):
    title = models.CharField(max_length = 200, null = False, blank = False)
    chapter = models.IntegerField(default = 1)
    url = models.TextField(default = "")
    Category = models.TextField(default = "")
    Author = models.CharField(max_length = 50, default = "")
    Uploaded_date = models.DateField(default = timezone.now())

    def __str__(self):
        return self.title


class Nanatsu(myManga):

    def get_absolute_url(self):
        return 'nanatsu/detail/'

class Overlord(myManga):

 
    def get_absolute_url(self):
        return 'overlord/detail/'

class Konosuba(myManga):

   

    def get_absolute_url(self):
        return 'konosuba/detail/'

class Onepunchman(myManga):

   
    def get_absolute_url(self):
        return 'onepunchman/detail/'
class Demon_Slayer(myManga):
   

    def get_absolute_url(self):
        return 'demonslayer/detail/'

class Prison_school(myManga):

    def get_absolute_url(self):
        return 'prisonschool/detail/'

class Conan(myManga):

    def get_absolute_url(self):
        return 'conan/detail/'