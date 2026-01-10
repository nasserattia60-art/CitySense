from django import forms
from .models import ReportFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ReportFeedback
        fields = ["accuracy", "usefulness", "clarity", "comment"]