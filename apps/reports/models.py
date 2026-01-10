from django.db import models
from django.conf import settings
from apps.analysis.models import AnalysisResult

User = settings.AUTH_USER_MODEL

class ReportAnalytics(models.Model):
    report = models.OneToOneField(AnalysisResult, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    feedback_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Analytics for Report {self.report.id}"
