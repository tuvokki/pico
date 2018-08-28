from django.urls import path
from django.conf.urls import url
from modernrpc.views import RPCEntryPoint

from . import views

app_name = 'haha'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    url(r'^rpc/', RPCEntryPoint.as_view()),
]
