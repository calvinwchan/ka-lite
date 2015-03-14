# Create your views here.
from django.http import HttpResponse
from annoying.decorators import render_to

@render_to('content/content.html')
def content_view(request):
    return {}