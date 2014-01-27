from django.test import TestCase

from quotes.models import Quote
# Create your tests here.

class QuoteMethodTests(TestCase):

	def setUp(self):
		self.quote = Quote(author="Lieke", quote="It's not a good day, it's raining!")

	def test_most_significant_word(self):
		self.assertEqual(self.quote.most_significant_word(), 'raining')

	def test_longest_word_double(self):
		quote_double = "It's double longes"
		double_word = max(quote_double.split(), key=len)
		self.assertEqual(double_word, 'double')
