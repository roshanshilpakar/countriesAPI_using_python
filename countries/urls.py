from django.conf.urls import url
from countries import views
import django.views.defaults

urlpatterns = [
    url(r'^api/countries$',views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_detail),
    url(r'^404/$', django.views.defaults.page_not_found, ),
    #url(r'^$', 'views.countries', name='home'),

]
