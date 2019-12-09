from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 200)
    spesies = models.CharField(max_length = 200)
    berat = models.CharField(max_length = 200)
    umur = models.IntegerField(default = 0)

    def __str__(self):
        return "Hewan : %s spesies %s dengan berat : %s dan umur : %d" %(self.nama, self.spesies, self.berat, self.umur)

class Kandang(models.Model):
    nama_kandang = models.CharField(max_length = 200)
    isi_kandang = models.IntegerField(default = 0)
    luas_kandang = models.CharField(max_length = 255)

    def __str__(self):
        return "Kandang : %s berisi %s binatang dengan luas kandang %s" %(self.nama_kandang, self.isi_kandang, self.luas_kandang)

class Penjaga(models.Model):
    nama_penjaga = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default=0)
    jadwal_jaga = models.DateTimeField('Jadwal Jaga: ')

    def __str__(self):
        return "Penjaga : %s dengan jadwal jaga : %s" %(self.nama_penjaga, self.jadwal_jaga)

class Pengunjung(models.Model):
    nama_pengunjung = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default=0)
    hari_berkunjung = models.DateTimeField('Hari Berkunjung: ')

    def __str__(self):
        return "Pengunjung : %s berkunjung pada hari: %s" %(self.nama_pengunjung,self.hari_berkunjung)