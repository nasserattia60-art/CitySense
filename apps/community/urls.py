from django.urls import path
from .views import feedback_view
app_name = "community"
urlpatterns = [
    path("feedback/<int:report_id>/", feedback_view, name="feedback"),
]