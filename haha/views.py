from django.views import generic

from .models import Joke


class IndexView(generic.ListView):
    template_name = 'haha/index.html'
    context_object_name = 'latest_jokes_list'

    def get_queryset(self):
        """ Return the last five jokes """
        return Joke.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Joke
    template_name = 'haha/detail.html'


class ResultsView(generic.DetailView):
    model = Joke
    template_name = 'haha/results.html'

