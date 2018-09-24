from modernrpc.core import rpc_method
from django.db.models import Max
from datetime import date
import random
import json

from .models import Joke


@rpc_method
def add(title, body, punchline):
    joke = Joke(title=title, body=body, punchline=punchline)
    joke.pub_date = date.today()
    joke.save()
    return json.dumps('ok')


@rpc_method
def last(number=5):
    last_jokes = Joke.objects.order_by('-pub_date')[:number]
    result_list = list(last_jokes.values('title', 'body', 'punchline'))  # 'pub_date' is not serializable
    return json.dumps(result_list)


@rpc_method(name='random')
def random_list(number=5):
    # Note: order_by('?') queries may be expensive and slow, depending on the database backend
    random_jokes = Joke.objects.all().order_by('?')[:number]
    result_list = list(random_jokes.values('title', 'body', 'punchline'))

    return json.dumps(result_list)
