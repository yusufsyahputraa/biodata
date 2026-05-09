from django.shortcuts import render, redirect
from .models import Kontak

def about_view(request):
    return render(request, 'about.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def motivasi_view(request):
    return render(request, 'motivasi.html')

def sertifikat(request):
    return render(request, 'sertifikat.html')

def kontak_view(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')

        Kontak.objects.create(nama=nama, email=email, pesan=pesan)
        messages.success(request, 'Pesan berhasil dikirim! Terima kasih')
        return redirect('kontak')

    return render(request, 'kontak.html')