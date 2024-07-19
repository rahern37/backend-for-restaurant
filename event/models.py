from django.db import models

class Event(models.Model):
	title=models.CharField(max_length=150)
	description=models.CharField(max_length=500)
	date=models.DateField()

	# string representation of the class
	def __str__(self):

		#it will return the title
		return self.title 
