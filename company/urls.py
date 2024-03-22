from .import views

from django.urls import path

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('company_retrieval/<int:pk>/', views.CompanyRetrieval.as_view()),
    path('achievement_retrieval/<int:pk>/',
         views.RetrieveAchievements.as_view()),
    path('woks_completed/<int:pk>/', views.RetrieveWorkCompleted.as_view())
]
