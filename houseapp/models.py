from django.db import models

# Create your models here.


class HousePrediction(models.Model):
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    sqft_living = models.IntegerField()
    sqft_lot = models.IntegerField()
    floors = models.FloatField()
    waterfront = models.IntegerField()
    view = models.IntegerField()
    condition = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    yr_built = models.IntegerField()
    yr_renovated = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    statezip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    predicted_price = models.FloatField()