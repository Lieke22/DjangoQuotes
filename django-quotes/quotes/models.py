from django.db import models
import string

# Create your models here.
class Quote(models.Model):
	author = models.CharField(max_length=150)
	quote = models.CharField(max_length=300, unique=True)
	image_url = models.CharField(max_length=300, blank=True, null=True)

	def __str__(self):
		return "%s %s %s" % (self.author, self.quote, self.image_url)

	def most_significant_word(self):
		longest_word = self.quote.translate(str.maketrans("","", string.punctuation))
		return max(longest_word.split(), key=len)
