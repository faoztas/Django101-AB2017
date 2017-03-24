from django.db import models

#Tuple Tanımı

SANAT_BOLUMLERI = (
    (1, 'Resim'),
    (2, 'Heykel'),
    (3, 'Muzik'),
    (4, 'Tiyatro')
)

# Create your models here.

class Kisi(models.Model):
    ad=models.CharField(max_length=30)
    soyad=models.CharField(max_length=30)
    eposta= models.EmailField(default='faoztas@gmail.com')

    def __str__(self):
        return str(self.eposta)

    class Meta:
        db_table="kisi_tablosu"
        verbose_name="Kisi"
        verbose_name_plural="Kisiler"

class Sanatci(models.Model):
    kisi = models.ForeignKey(Kisi)
    ilgilendigi_bolum = models.IntegerField(choices=SANAT_BOLUMLERI)

    def __str__(self):
        return str(self.kisi)

    class Meta:
        verbose_name="Sanatci"
        verbose_name_plural="Sanatciler"