from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_list),
    path('create/', views.user_create),
    path('update/<int:id>/', views.user_update),
    path('delete/<int:id>/', views.user_delete),
]
