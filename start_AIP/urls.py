
from django.contrib import admin
from django.urls import path , include
from app.views import employeeListView , home_page , UserListView , employeeDetailView

urlpatterns = [
    path('' , home_page),
    path('admin/', admin.site.urls),
    path('api/employees' , employeeListView),
    path('api/employees/<int:pk>' , employeeDetailView),
    path('api/users' , UserListView),
]
