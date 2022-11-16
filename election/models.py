from distutils.command.upload import upload
from django.db import models

class Candidate(models.Model):
    number = models.IntegerField('候補者No.',default=1)
    name = models.CharField('名前',max_length=30)
    Political = models.CharField('政党',max_length=30)
    description = models.TextField('説明',default="",blank=True)
    image = models.ImageField(upload_to = 'images',verbose_name='顔写真',null=True,blank=True)
    vote = models.IntegerField('票数',default=0)
    
    def __str__(self):
        return self.name

class Vote(models.Model):
    vote_id = models.CharField(default=1,primary_key=True,max_length=3)



# Create your models here.
