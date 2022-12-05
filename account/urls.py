from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

from . import views

urlpatterns = [
    path('register/',  views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]
