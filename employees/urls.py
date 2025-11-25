from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.employee_detail,name='employee_detail'),
    path('add/',views.add_employee,name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
