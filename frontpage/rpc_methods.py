from modernrpc.core import rpc_method
import json
from .models import Hero
from datetime import date


@rpc_method
def fetchHero(id=1):
    hero = Hero.objects.get(id)
    return json.dumps(hero.values('image', 'head', 'sub', 'link', 'linktext', 'slot'))
