from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default = 0)
    bidang = models.CharField(max_length = 200)
    jadwal_praktek = models.DateTimeField('Jadwal Praktek')

    def __str__(self):
        return "Dokter : %s dalam bidang %s dengan jadwal praktek: %s" %(self.nama,self.bidang,self.jadwal_praktek)

class Pasien(models.Model):
    nama_pasien = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default = 0)
    alamat = models.CharField(max_length = 255)
    keluhan = models.CharField(max_length = 200)

    def __str__(self):
        return "Pasien : %s memiliki keluhan %s" %(self.nama_pasien, self.keluhan)

class Resep(models.Model):
    nama_resep = models.CharField(max_length = 200)
    total_harga = models.IntegerField(default=0)
    kumpulan_obat = models.CharField(max_length = 200)

    def __str__(self):
        return "Resep : %s dengan total harga : %s" %(self.nama_resep, self.total_harga)

class Obat(models.Model):
    nama_obat = models.CharField(max_length = 200)
    kandungan = models.CharField(max_length = 200)
    khasiat = models.CharField(max_length = 200)

    def __str__(self):
        return "Obat : %s dengan kandungan %s berkhasiat untuk %s" %(self.nama_obat,self.kandungan, self.khasiat)