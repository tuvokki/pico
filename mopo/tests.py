import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Quote


class QuotesModelTest(TestCase):

    def test_was_published_recently_with_future_quote(self):
        """
        was_published_recently() returns False for quotes whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quote = Quote(pub_date=time)
        self.assertIs(future_quote.was_published_recently(), False)

    def test_was_published_recently_with_old_quote(self):
        """
        was_published_recently() returns False for quotes whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_quote = Quote(pub_date=time)
        self.assertIs(old_quote.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_quote(self):
        """
        was_published_recently() returns True for quotes whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_quote = Quote(pub_date=time)
        self.assertIs(recent_quote.was_published_recently(), True)


def create_quote(quote_text, days):
    """
    Create a quote with the given `quote_text` and published the
    given number of `days` offset to now (negative for quotes published
    in the past, positive for quotes that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Quote.objects.create(quote_text=quote_text, pub_date=time)


class QuoteIndexViewTests(TestCase):
    def test_no_quotes(self):
        """
        If no quotes exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('mopo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Motivational Posters are available.")
        self.assertQuerysetEqual(response.context['poster_list'], [])

    def test_past_quote(self):
        """
        Quotes with a pub_date in the past are displayed on the
        index page.
        """
        create_quote(quote_text="Past quote.", days=-30)
        response = self.client.get(reverse('mopo:index'))
        self.assertQuerysetEqual(
            response.context['poster_list'],
            ['<Quote: Past quote.>']
        )

    def test_future_quote(self):
        """
        Quotes with a pub_date in the future aren't displayed on
        the index page.
        """
        create_quote(quote_text="Future quote.", days=30)
        response = self.client.get(reverse('mopo:index'))
        self.assertContains(response, "No Motivational Posters are available.")
        self.assertQuerysetEqual(response.context['poster_list'], [])

    def test_future_quote_and_past_quote(self):
        """
        Even if both past and future quotes exist, only past quotes
        are displayed.
        """
        create_quote(quote_text="Past quote.", days=-30)
        create_quote(quote_text="Future quote.", days=30)
        response = self.client.get(reverse('mopo:index'))
        self.assertQuerysetEqual(
            response.context['poster_list'],
            ['<Quote: Past quote.>']
        )

    def test_two_past_quotes(self):
        """
        The quotes index page may display multiple quotes.
        """
        create_quote(quote_text="Past quote 1.", days=-30)
        create_quote(quote_text="Past quote 2.", days=-5)
        response = self.client.get(reverse('mopo:index'))
        self.assertQuerysetEqual(
            response.context['poster_list'],
            ['<Quote: Past quote 2.>', '<Quote: Past quote 1.>']
        )


class QuoteDetailViewTests(TestCase):
    def test_future_quote(self):
        """
        The detail view of a quote with a pub_date in the future
        returns a 404 not found.
        """
        future_quote = create_quote(quote_text='Future quote.', days=5)
        url = reverse('mopo:detail', args=(future_quote.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_quote(self):
        """
        The detail view of a quote with a pub_date in the past
        displays the quote's text.
        """
        past_quote = create_quote(quote_text='Past Quote.', days=-5)
        url = reverse('mopo:detail', args=(past_quote.id,))
        response = self.client.get(url)
        self.assertContains(response, past_quote.quote_text)