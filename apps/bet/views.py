from django.views.generic.edit import FormView
from forms import NormalBetForm


class NormalBetView(FormView):
    template_name = 'normal_bet.html'
    form_class = NormalBetForm
    success_url = '/'

    def form_valid(self, form):
        return super(NormalBetView, self).form_valid(form)
