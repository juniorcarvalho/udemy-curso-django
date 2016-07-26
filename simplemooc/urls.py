from simplemooc.core.views import home, contact
from simplemooc.courses.views import courses, details
from simplemooc.accounts.views import register
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),


    url(r'^contato/$', contact, name='contact'),
    url(r'^cursos/', courses, name='courses'),

    url(r'^entrar/$', login,
        {'template_name': 'login.html'}, name='login'),

    url(r'^sair/', logout,
        {'next_page': 'home'}, name='logout'),

    url(r'^cadastro/$', register, name='register'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
