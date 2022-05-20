from django.db import models
# from django.contrib.auth.models import User     
from members.models import User        
from django.urls import reverse	

# Create your models here.
class Survey(models.Model):
	question = models.CharField(null=True, blank=True, max_length=255)
	extra_info = models.CharField(null=True, blank=True, max_length=1000)
	likes = models.ManyToManyField(User, blank=True ,related_name='likes')
	dislikes = models.ManyToManyField(User, blank=True ,related_name='dislikes')  

	# def get_absolute_url(self):
	# 	return reverse('surveys', args=[str(self.id)])
	
	def num_likes(self):
		return self.likes.count()

	def num_dislikes(self):
		return self.dislikes.count()