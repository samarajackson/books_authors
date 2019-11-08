from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.addbook, name="addbook"),
    url(r'^books/(?P<book_id>\d)+$', views.book),
    url(r'^authors$', views.authors),
    url(r'^addauthor$', views.addauthor),
    url(r'^authors/(?P<author_id>\d)+$', views.authordeets),
    url(r'^addauthortobook/(?P<author_id>\d)/(?P<book_id>\d)$', views.linkauthor),
    url(r'^addbooktoauthor/(?P<author_id>\d)/(?P<book_id>\d)$', views.linkbook),
] 