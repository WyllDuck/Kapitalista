from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'graph'
urlpatterns = [
    # AJAX logic graph_2
    url(r'^2$', views.graph_2, name = "graph_2"),
    url(r'^graph_6_AJAX$', views.graph_6_AJAX, name = "graph_6_AJAX"),

    # No AJAX in graph_3
    url(r'^3/(?P<incomes>[-\w]+)/(?P<subjects_list>[-\w]+)/(?P<postal_code>[-\w]+)$', views.graph_3, name = "graph_3"),

    # AJAX logic graph_1    
    url(r'^graph_1_AJAX$', views.graph_1_AJAX, name = "graph_1_AJAX"),
    url(r'^graph_5_AJAX$', views.graph_5_AJAX, name = "graph_5_AJAX"),
    url(r'^1$', views.graph_1, name = "graph_1")  
    
]
