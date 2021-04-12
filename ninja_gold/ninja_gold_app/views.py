from django.shortcuts import render, redirect
from random import randrange
from time import gmtime, strftime

def index(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'gold' : request.session['gold_amount']
    }
    return render(request, "index.html", context)


def proccess_money(request, location):
    gold = 0
    activity = ''
    time = strftime("%d-%m-%Y %I:%M %p %a", gmtime())
    if location == 'farm':
        gold = randrange(10,20)
    elif location == 'casino':
        gold = randrange(-50,50)
    elif location == 'cave':
        gold = randrange(5,10)
    elif location == 'house':
        gold = randrange(2,5)
    if gold > 0:
        activity = f'Earned {gold} in {location} ({time}).'
        color = 'green'
    else:
        activity = f'Entered {location} and lost {gold} ({time}).'
        color = 'red'
    request.session['gold_amount'] += gold
    
    request.session['activities'].append({'color' : color, 'activity':activity, 'time':time})
    return redirect('/')

def clean(request):
    del request.session['gold_amount']
    del request.session['activities']
    return redirect('/')