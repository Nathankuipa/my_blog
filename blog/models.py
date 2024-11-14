from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.												CharField(max_length=200)
	slug = models.SlugField(max_length = 200,default = title)
	content = models.TextField()
	created_at = models.DateTimeField(default = timezone.now)
	
	def __str__(self):
		return self.title