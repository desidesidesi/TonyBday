from django.conf.urls import include, url
from django.contrib import admin
from bday import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^toni/$', views.happy_bday),
    url(r'^wishes/$', views.wishes),
    url(r'^more/$', views.more),
    url(r'^we/$', views.we),
    url(r'^calendar/', include('bday.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
