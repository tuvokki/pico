from django.conf.urls import url
from modernrpc.views import RPCEntryPoint

from . import views

app_name = 'frontpage'
urlpatterns = [
    url(r'^rpc/', RPCEntryPoint.as_view()),
]
