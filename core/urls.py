"""
URL configuration for school_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from student_app import views
from library_app import urls
from school_site import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-techer/', views.show_teacher_info, name='show_teacher_info'),
    path('school/', include(urls)),
    path('library/',include('library_app.urls')),
]