from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from weightStation import views

urlpatterns = [
    path('weight-station/live-weight', views.LiveWeight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)