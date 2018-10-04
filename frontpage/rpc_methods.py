from django.core import serializers
from modernrpc.core import rpc_method

from .models import Hero

fields = ('head', 'image', 'sub', 'link', 'linktext', 'slot')


@rpc_method(name='fetchhero')
def fetch_hero(id=1):
    return serializers.serialize('json', Hero.objects.filter(pk=id), fields=fields)


@rpc_method(name='randomhero')
def rnd_hero():
    return serializers.serialize('json', Hero.objects.all().order_by('?')[:1], fields=fields)
