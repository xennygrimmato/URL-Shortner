from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import bitly
import re

def validate_url(url):
	regex = re.compile(
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|' #localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?' # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	if regex.match(url):
		return True
	else:
		return False


@csrf_exempt
def shorten_url(url):
	if validate_url(url):
		api = bitly.Api(login='login', apikey='apikey')
		short = api.shorten(url)
		return short
	else:
		return 'Invalid URL'

def get_shortened_url(url):
    shortened_url = shorten_url(url)
    return shortened_url

def render_p1(request):
    return render(request,'p1.html')

@csrf_exempt
def render_p2(request):
    url = str(request.POST['url'])
    #print url
    shortened_url = get_shortened_url(url)
    return render(request,'short.html',{'url':shortened_url})
