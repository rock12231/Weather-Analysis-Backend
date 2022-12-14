from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    path('api/snippet/', views.SnippetList.as_view()),
    path('api/snippet/<int:pk>/', views.SnippetDetail.as_view()),
    path('api/df/', views.DFList.as_view()),
    path('api/df/<str:pk>/', views.DFDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)