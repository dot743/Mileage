from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MileageUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mileage_user')

	@property
	def last_date(self):
		if len(self.trips.all()) > 0:
			return self.trips.latest('date').date
		return None

class Place(models.Model):
	name = models.CharField(max_length=64)
	abbr = models.CharField(max_length=5)

	def __str__(self):
		return self.name


class Trip(models.Model):
	mileage_user = models.ForeignKey(MileageUser, on_delete=models.CASCADE, related_name='trips')
	date = models.DateField()


class Stop(models.Model):
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	number = models.IntegerField()

	class Meta:
		unique_together = (('number', 'trip'),)
