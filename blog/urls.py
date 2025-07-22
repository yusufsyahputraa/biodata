
from django.contrib import admin
from django.urls import path, include
from self import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),
    path('about/', views.about_view, name='home'),
    path('kontak/', views.kontak_view, name='kontak'),
    path('motivasi/', views.motivasi_view, name='motivasi'),
    path('', include('self.urls')),
]
