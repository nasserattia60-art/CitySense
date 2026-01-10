from django.urls import path
from .views import analyze_view, report_view , heatmap_data , city_suggestions
app_name = "analysis"
urlpatterns = [
    path("", analyze_view, name="analyze"),
    path("report/<int:pk>/", report_view, name="report"),
    path("heatmap-data/", heatmap_data, name="heatmap-data"),
    path("ajax/city_suggestions/", city_suggestions, name="city_suggestions"),
]