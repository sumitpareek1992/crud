"""vs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main.views import home_view, create_view
from django.views.generic import UpdateView, DeleteView
from main.models import Emp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('create', create_view,name='create'),
    path('update/<int:pk>', UpdateView.as_view(
    	model = Emp,
    	fields = "__all__",
    	success_url = '/home/',
    	template_name='update.html')),
    path('delete/<int:pk>', DeleteView.as_view(
    	model= Emp,
    	success_url='/home/',
    	template_name='delete.html'))
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)