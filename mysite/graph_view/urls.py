from django.conf.urls import url
from . import views

app_name = 'graph'
urlpatterns = [
    url(r'^/1$', views.graph_1, name = "graph_1"),
    url(r'^/2$', views.graph_2, name = "graph_2"),
    url(r'^/3$', views.graph_3, name = "graph_3"),
    url(r'^/general_view$', views.general, name = "graph_general"),    
]