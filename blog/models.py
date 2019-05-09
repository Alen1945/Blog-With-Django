from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
	slug=models.SlugField(blank=True,editable=False,unique=True)

	def save(self,*args,**kwargs):
		self.slug=slugify(self.title)
		super().save()
	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('blog:post-detail',kwargs={'slug':self.slug})