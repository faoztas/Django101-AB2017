# Django101-AB2017
Examples for Python and Django 

django-admin startproject proje_adi --> Django projesi oluşturma kodu

python manage.py runserver --> projeyi serverda koşma komutu

python manage.py startapp app_adi --> projenin altında yeni bir app oluşturmak için

python manage.py test --> testi deneme kodu

Kaynaklar:

https://docs.djangoproject.com/en/1.10/intro/tutorial01/

https://tutorial.djangogirls.org/tr/index.html

http://www.pythondersleri.com/p/django-egitim-serisi.html



----2----




python manage.py makemigrations                               --> oluşturma

python manage.py migrate (python manage.py migrate model_app) --> uygulama

python manage.py showmigrations --> tüm migrations görme

python manage.py sqlmigrate model_app 0001_initial            --> oluşan sql'i görmek için

    class Meta:
        db_table="kisi_tablosu"                               --> tablo adı değiştirme


python manage.py shell                                        --> teste yazmadan test etmek için(mesela views)

python manage.py createsuperuser                              --> admin paneline yetkili atama

**********

>>> from model_app.models import Kisi,Sanatci
>>> kisi=Kisi()
>>> print(kisi)
Kisi object
>>> kisi.ad = "Ahmet Can"
>>> kisi.soyad="kepenek"
>>> kisi.eposta
'faoztas@gmail.com'
>>> kisi.epsota="ahmet.can@gmail.com"
>>> kisi.eposta
'faoztas@gmail.com'
>>> kisi.eposta="ahmet.can@gmail.com"
>>> kisi.eposta
'ahmet.can@gmail.com'
>>> kisi.save()
>>> kisi.id
1

--------------------

>>> sanatci=Sanatci()
>>> sanatci.ilgilendigi_bolum =1
>>> sanatci.kisi=kisi
>>> sanatci.save()
>>> sanatci.id
1


***************



netstat -ap |grep 8000










Proje CollectiveWork

iş ---> kullanıcı

*user profile app

-kullanıcı ekle
-kullanıcı profili

*ticket app


python -m smtpd -n -c DebuggingServer localhost:1025 --> mesaj almak için gerekli olan EMAIL sunucusu açılıyor

