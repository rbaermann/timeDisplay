from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    return render(request, 'app1/index.html', context)
