from simplemooc.core.views import home, contact
from simplemooc.courses.views import courses, details
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^cursos/', courses, name='courses'),
    #url(r'^(?P<pk>\d+)/$', details, name='details')
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
