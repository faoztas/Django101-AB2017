from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def merhaba(request):
    print("body: %s " % request.body)
    print("path: %s " % request.path)
    print("content_type %s " % request.content_type)
    print("META %s " % request.META)
    return HttpResponse("Merhaba Dunya")

def toplama(request):
    sayi1 = 10
    sayi2 = 20
    return HttpResponse(sayi1+sayi2)

def merhaba_html(request):
    response = HttpResponse()
    response.write("<h1>Django Kursu</h1>")
    response.write("<p>Akademik Bilisim</p>")
    return response

