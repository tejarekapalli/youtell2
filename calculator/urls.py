from django.urls import path
from calculator import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('master_dashboard/', views.master_dashboard, name='master_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('create_calculation/', views.create_calculation, name='create_calculation'),
    path('activity_log/', views.activity_log, name='activity_log'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
