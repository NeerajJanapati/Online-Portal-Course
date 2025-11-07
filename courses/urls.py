"""
Course Portal URL Configuration
URL routing patterns for the courses application
"""

from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Instructor dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-course/', views.add_course, name='add_course'),

    # Course details
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]