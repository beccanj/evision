"""
URL configuration for evision project.

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views
from main.views import blogs, blog_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('route', views.routeplanner, name='routeplanner'),
    path('featured', views.featured, name='featured'),
    path('getfeatured', views.getfeatured, name='getfeatured'),
    path('blogs/', blogs, name='blogs'),

    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('about', views.about, name='about'),
    path('whyus', views.whyevision, name='whyevision'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
