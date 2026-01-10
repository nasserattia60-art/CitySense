from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.analysis.models import AnalysisResult

@login_required
def reports_list_view(request):
    reports = AnalysisResult.objects.filter(user=request.user)
    return render(request, "reports/list.html", {"reports": reports})