from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default = 0)
    jabatan = models.CharField(max_length = 200)

    def __str__(self):
        return "Direksi : %s dengan jabatan: %s" %(self.nama_lengkap,self.jabatan)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default = 0)
    nomor_absen = models.IntegerField(default = 0)
    nilai_ratarata = models.FloatField(default = 0)

    def __str__(self):
        return "Mentee : %s dengan nomor absen %s memiliki nilai rata-rata %s" %(self.nama_lengkap, self.nomor_absen, self.nilai_ratarata)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 200)
    jadwal_dimulai = models.DateTimeField('Jadwal Dimulai')
    jadwal_berakhir = models.DateTimeField('Jadwal Berakhir')

    def __str__(self):
        return "Mata Pelajaran : %s dengan jadwal : %s hingga %s" %(self.nama_pelajaran,self.jadwal_dimulai, self.jadwal_berakhir)

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length = 200)
    nomor_telepon = models.IntegerField(default = 0)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Mentor : %s mengajar : %s" %(self.nama_mentor, self.mata_pelajaran)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 200)
    banyak_soal = models.IntegerField(default = 0)
    bobot_nilai = models.CharField(max_length = 200)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Challenge : %s dengan banyak soal %s dengan bobot nilai %s" %(self.nama_challenge,self.banyak_soal, self.bobot_nilai)

class LiveCode(models.Model):
    nama_livecode = models.CharField(max_length = 200)
    banyak_soal = models.IntegerField(default = 0)
    bobot_nilai = models.IntegerField(default = 0)
    tanggal_pelaksanaan = models.DateTimeField('Tanggal Pelaksanaan: ')
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Live Code : %s dengan banyak soal %s pada tanggal %s" %(self.nama_livecode,self.banyak_soal, self.tanggal_pelaksanaan)