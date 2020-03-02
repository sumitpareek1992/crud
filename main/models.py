from django.db import models

# Create your models here.
class Emp(models.Model):
	emp_id = models.CharField(max_length=20)
	email = models.EmailField(max_length=40)
	username = models.CharField(max_length=25)
	password = models.CharField(max_length=10)
	dob = models.DateField()
	pic = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.email


