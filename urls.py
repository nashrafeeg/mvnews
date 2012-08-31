from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import apps.request
import apps.Profiles
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static


handler500 = "pinax.views.server_error"


urlpatterns = patterns( "",
    url( r"^$", direct_to_template, {
        "template": "homepage/home.html",
    }, name="home" ),
    url( r"^admin/", include( admin.site.urls ) ),
    url( r"^profile/", include( 'Profiles.urls' ) ),
    url( r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog' ),
 ) + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


if settings.SERVE_MEDIA:
    urlpatterns += patterns( "",
        url( r"", include( "staticfiles.urls" ) ),
    )
