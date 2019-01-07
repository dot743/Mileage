from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create_trip', views.create_trip, name='create_trip'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('view_mileage/', views.view_mileage, name='view_mileage'),
]
