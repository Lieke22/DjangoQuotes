from django.contrib import admin
from quotes.models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
	fields = ['author', 'quote', 'image_url']
	list_display = ('author', 'quote', 'image_url')
	search_fields = ['author', 'quote']

admin.site.register(Quote, QuoteAdmin)