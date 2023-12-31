"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import create_assignment, assignment_list, complete_assignment, submit_assignment

urlpatterns = [
    path('', assignment_list, name='home'),  # Add this line
    path('create-assignment/', create_assignment, name='create_assignment'),
    path('assignment-list/', assignment_list, name='assignment_list'),
    path('complete-assignment/<int:assignment_id>/', complete_assignment, name='complete_assignment'),
    path('submit-assignment/<int:assignment_id>/', submit_assignment, name='submit_assignment'),
]
