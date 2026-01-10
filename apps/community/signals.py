from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReportFeedback

@receiver(post_save, sender=ReportFeedback)
def update_report_score(sender, instance, **kwargs):
    report = instance.report
    feedbacks = ReportFeedback.objects.filter(report=report)

    report.avg_feedback_score = round(
        sum(f.quality_score() for f in feedbacks) / feedbacks.count(), 2
    )
    report.save()