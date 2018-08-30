from modernrpc.core import rpc_method
import json
from .models import Joke


@rpc_method
def add(a, b):
    return a + b


@rpc_method
def last():
    last_jokes = Joke.objects.order_by('-pub_date')[:5]
    # return json.dumps(last_jokes, indent=4, sort_keys=True, default=str)
    result_list = list(last_jokes.values('title', 'body', 'punchline'))  # 'pub_date' is not serializable
    return json.dumps(result_list)
