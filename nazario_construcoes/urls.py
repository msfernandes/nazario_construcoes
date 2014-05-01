from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

from foundation import urls

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'nazario_construcoes.views.home',
                       # name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^relatorios/', include('relatorios.urls')),

                       #url(r'^foundation/', include(urls)),

                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^', 'relatorios.views.home')

                       )
