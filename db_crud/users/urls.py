from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('register/', views.user_register),
    path('login/', views.user_login),
    path('update/<int:id>/', views.user_update),
    path('user/delete/<int:id>/', views.user_delete),
]
