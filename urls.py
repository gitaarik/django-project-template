from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    url('^grappelli/', include('grappelli.urls')),
    url('^admin/doc/', include('django.contrib.admindocs.urls')),
    url('^admin/', include(admin.site.urls)),
]
