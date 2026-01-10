from django.db import models
from django.conf import settings
from apps.analysis.models import AnalysisResult


# Create your models here.

User = settings.AUTH_USER_MODEL

class ReportFeedback(models.Model):
    report = models.ForeignKey(AnalysisResult, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    accuracy = models.IntegerField(help_text="1-5")
    usefulness = models.IntegerField(help_text="1-5")
    clarity = models.IntegerField(help_text="1-5")

    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def quality_score(self):
        return round(
            (self.accuracy + self.usefulness + self.clarity) / 3, 2
        )

    def __str__(self):
        return f"Feedback for Report {self.report.id}"