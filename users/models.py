import os
import time
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	def image_path(instance,imagename):
		base_name,ext=os.path.splitext(imagename)
		return f"profile_pics/{time.strftime('%y%m%d%H%M%S')}_{base_name[0:5]}{ext}"
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to=image_path)


	def __str__(self):
		return f'{self.user.username} Profile'
	def save(self,*args,**kwargs):
		super().save()
		img=Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

		
