from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView


class RedirectTweetsListView(RedirectView):
    url = reverse_lazy('tweets:list')

class TweetsListView(TemplateView):
    template_name = 'comment.html'
