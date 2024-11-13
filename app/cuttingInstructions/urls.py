from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cuttingInstructions import views

urlpatterns = [
    path('cutting-instructions/', views.CuttingInstructionList.as_view()),
    path('cutting-instructions/<int:pk>', views.CuttingInstructionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)