from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from apps.analysis.models import AnalysisResult


# Create your views here.

@login_required
def feedback_view(request, report_id):
    report = AnalysisResult.objects.get(id=report_id)
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user
        feedback.report = report
        feedback.save()
        return redirect("report", report.id)

    return render(request, "community/feedback.html", {
        "form": form,
        "report": report
    })