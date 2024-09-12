from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scheduler import views

urlpatterns = [
    path('scheduler/events', views.EventList.as_view()),
    path('scheduler/events/<int:pk>', views.EventList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)