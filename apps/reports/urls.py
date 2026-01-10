from django.urls import path
from .views import reports_list_view
app_name = "reports"
urlpatterns = [
    path("", reports_list_view, name="reports"),
]
