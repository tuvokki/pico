from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import get_object_or_404, render
from .models import Quote, Comment


def index(request):
    poster_list = Quote.objects.order_by('-pub_date')[:5]
    context = {'poster_list': poster_list}
    return render(request, 'mopo/index.html', context)


def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'mopo/detail.html', {'quote': quote})


def summary(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'mopo/summary.html', {'quote': quote})


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
