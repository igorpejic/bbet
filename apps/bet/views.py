import datetime

from django.views.generic.edit import FormView
from django.shortcuts import render_to_response

from forms import NormalBetForm
from models import Week, Position


class NormalBetView(FormView):
    template_name = 'normal_bet.html'
    form_class = NormalBetForm
    success_url = '/'

    def form_valid(self, form):
        return super(NormalBetView, self).form_valid(form)


def current_week(request):
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    print sunday
    week = Week.objects.get(date=sunday)
    songs = Position.objects.filter(week=week)

    return render_to_response('normal_bet.html', {'songs': songs})
