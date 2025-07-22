from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('', views.dashboard_view, name='dashboard'),
    path('kontak/',views.kontak_view, name='kontak'),
    path('motivasi/',views.motivasi_view, name='motivasi'),

]
