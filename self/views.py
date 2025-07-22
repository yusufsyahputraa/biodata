from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')

def kontak_view(request):
    return render(request, 'kontak.html')

def motivasi_view(request):
    return render(request, 'motivasi.html')