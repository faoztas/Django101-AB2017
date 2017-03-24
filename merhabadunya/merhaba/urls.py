from django.conf.urls import url, include

from merhaba import views

urlpatterns=[
    url(r'^$', views.merhaba),
    url(r'^toplama',views.toplama),
    url(r'^merhaba',views.merhaba_html)
]