from django.db import models

# Create your models here.

class Blog(models.Model):
	"""docstring for Blog"""
	Name= models.CharField(max_length=30)
	Rolno= models.CharField(max_length=30)
	dep= models.CharField(max_length=30)
	mark1=models.IntegerField()
	mark2=models.IntegerField()
	mark3=models.IntegerField()
	mark4=models.IntegerField()

	class Meta:
		db_table = 'stud'  #table name
		