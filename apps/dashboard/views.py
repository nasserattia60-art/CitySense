from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.analysis.models import AnalysisResult

@login_required
def dashboard_view(request):
    reports = AnalysisResult.objects.filter(user=request.user)

    context = {
        "reports_count": reports.count(),
        "avg_ai_score": round(
            sum(r.ai_score for r in reports) / reports.count(), 2
        ) if reports else 0,
        "latest_reports": reports.order_by("-created_at")[:5],
    }

    return render(request, "dashboard/dashboard.html", context)




@login_required
def map_view(request):
    return render(request, "dashboard/map.html")