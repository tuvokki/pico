from modernrpc.core import rpc_method
import json
from .models import Joke
from datetime import date

@rpc_method
def add(title, body, punchline):
    joke = Joke(title=title, body=body, punchline=punchline)
    joke.pub_date = date.today()
    joke.save()
    return json.dumps('ok')


@rpc_method
def last(number=5):
    last_jokes = Joke.objects.order_by('-pub_date')[:number]
    # return json.dumps(last_jokes, indent=4, sort_keys=True, default=str)
    result_list = list(last_jokes.values('title', 'body', 'punchline'))  # 'pub_date' is not serializable
    return json.dumps(result_list)
