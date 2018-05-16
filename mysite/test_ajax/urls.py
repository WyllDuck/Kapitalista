from django.conf.urls import url
from . import views

app_name = 'test'

urlpatterns = [
    url(r'^graph_1_AJAX$', views.graph_1_AJAX, name = "graph_1_AJAX"),
    url(r'^graph_1$', views.graph_1, name = "graph_1")        
]