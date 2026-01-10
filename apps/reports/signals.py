from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.analysis.models import AnalysisResult
from .models import ReportAnalytics

@receiver(post_save, sender=AnalysisResult)
def create_analytics(sender, instance, created, **kwargs):
    if created:
        ReportAnalytics.objects.create(report=instance)