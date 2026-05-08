from django.db import models

class Kontak(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama