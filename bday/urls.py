from django.conf.urls import url
from bday import views

urlpatterns = [
    url(r'^toni/$', views.happy_bday),
    url(r'^wishes/$', views.wishes),
]
