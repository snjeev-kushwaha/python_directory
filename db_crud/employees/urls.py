from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('create/', views.employee_create),
    path('update/<int:id>/', views.employee_update),
    path('delete/<int:id>/', views.employee_delete),
]
