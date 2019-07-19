"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from petapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('petshop/list/',views.pet_list ,name='pet-list'),
    path('petshop/create/',views.pet_create ,name='pet-create'),
    path('petshop/detail/<int:pet_id>/',views.pet_detail ,name='pet-detail'),
    path('petshop/update/<int:pet_id>/',views.pet_update ,name='pet-update'),
    path('petshop/delete/<int:pet_id>/',views.pet_delete ,name='pet-delete'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)