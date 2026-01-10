from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Location(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address



class AnalysisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    safety_score = models.FloatField()
    noise_level = models.CharField(max_length=50)
    rent_level = models.CharField(max_length=50)
    water_quality = models.CharField(max_length=50)

    ai_summary = models.TextField()
    ai_score = models.IntegerField()
    avg_feedback_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    temperature = models.FloatField(null=True, blank=True)
    windspeed = models.FloatField(null=True, blank=True)
    weather_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.location} - {self.ai_score}"