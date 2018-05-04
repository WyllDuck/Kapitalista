from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'graph'
urlpatterns = [
    url(r'^1/(?P<subject_code>[0-9]{6})$', views.graph_1, name = "graph_1"),
    url(r'^2/(?P<incomes>[-\w]+)$', views.graph_2, name = "graph_2"),
    url(r'^3/(?P<incomes>[-\w]+)$', views.graph_3, name = "graph_3"),
    url(r'^general_view/(?P<postal_code>[-\w]+)$', views.general, name = "graph_general"),
]
