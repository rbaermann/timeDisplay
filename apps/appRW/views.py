from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    context = {}
    request.session['count'] += 1
    context['count'] = request.session['count']
    context['random'] = get_random_string(length=14)
    return render(request, 'appRW/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/random_word')