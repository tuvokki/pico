from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Quote, Comment


class IndexView(generic.ListView):
    template_name = 'mopo/index.html'
    context_object_name = 'poster_list'

    def get_queryset(self):
        """Return the last five published quotes (not including those set to be
        published in the future)."""
        return Quote.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Quote
    template_name = 'mopo/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Quote.objects.filter(pub_date__lte=timezone.now())


class SummaryView(generic.DetailView):
    model = Quote


def comment(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'mopo/comment.html', {'quote': quote})


def vote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    try:
        upvote_comment = quote.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the quote voting form.
        return render(request, 'mopo/detail.html', {
            'quote': quote,
            'error_message': "You didn't select a choice.",
        })
    else:
        upvote_comment.votes += 1
        upvote_comment.save()
        return HttpResponseRedirect(reverse('mopo:detail', args=(quote.id,)))
