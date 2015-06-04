import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import NormalBetForm
from models import Week, Position


def normal_bet(request):
    if request.method == 'POST':
        form = NormalBetForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')
    template_name = 'bet/normal_bet.html'
    form = NormalBetForm
    success_url = '/'
    print 'called'

    return render(request, template_name, {'form': form})


def current_week(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/bet/week/')
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    print sunday
    week = Week.objects.get(date=sunday)
    songs = Position.objects.filter(week=week)

    return render(request, 'bet/normal_bet.html', {'songs': songs})
