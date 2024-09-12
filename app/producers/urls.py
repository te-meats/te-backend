from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from producers import views

urlpatterns = [
    path('producers/', views.ProducerList.as_view()),
    path('producers/<int:pk>', views.ProducerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)