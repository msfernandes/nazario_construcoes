from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('relatorios.views',
                       # Examples:
                       # url(r'^$', 'nazario_construcoes.views.home',
                       # name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'home'),
                       url(r'^contatos/$', 'contatos'),
                       url(r'^obras/$', 'obras'),
                       url(r'^resumo/$', 'resumo_obra'),
                       )
