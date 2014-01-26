from django.db import models



# Create your models here.
class Quote(models.Model):
	author = models.CharField(max_length=150)
	quote = models.CharField(max_length=300)
	image_url = models.CharField(max_length=300, blank=True, null=True)

	def __str__(self):
		return "%s %s %s" % (self.author, self.quote, self.image_url)

	