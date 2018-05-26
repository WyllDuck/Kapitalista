from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^conclusion$', views.conclusion, name = "conclusion"),
    url(r'^postal_code$', views.postal_code_AJAX, name = "postal_code"),      
]