from django.shortcuts import render
from django.http import HttpResponse
from quotes.models import Quote
from django.template import RequestContext, loader
from django.http import Http404

def index(request):
    random_quote = Quote.objects.order_by('?')[0]
    context = {'random_quote': random_quote}
    return render(request, 'quotes/index.html', context)

def detail(request, quote_id):
	try:
		quote = Quote.objects.get(pk=quote_id)
	except Quote.DoesNotExist:
		raise Http404
	return render(request, 'quotes/detail.html', {'quote': quote})


def results(request, quote_id):
    return HttpResponse("This is quote  %s." % quote_id)

def vote(request, quote_id):
    return HttpResponse("You're voting on quote %s." % quote_id)

