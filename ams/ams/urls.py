"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from assignment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('show/', views.show, name='show'),
    path('show/tech/', views.tech, name='tech'),
    path('delete/<int:pk>/', views.delete, name='delete'),

    path('class/tech/', views.TeacherListView.as_view(), name='class_tech'),
    path('class/tech/upload/', views.UploadTeacherView.as_view(), name=''),
    path('show1/', views.show1, name='show1'),
    path('show1/stud/', views.stud, name='stud'),
    path('delete1/<int:pk>/', views.delete1, name='delete1'),

    path('class/stud/', views.StudentListView.as_view(), name='class_stud'),
    path('class/stud/upload/', views.UploadStudentView.as_view(), name=''),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
