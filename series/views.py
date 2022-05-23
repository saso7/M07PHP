from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from series.models import Serie, Episode


class SerieView(View):

        def get(self, request):
            if request.user.is_authenticated:
                context = {
                    'series': list(Serie.objects.all())
                }
                return render(request, 'series.html', context=context)
            return redirect('login')


class EpisodeView(LoginRequiredMixin, View):


    def get(self, request, serie_id:int):
        context = {
            'episodes': list(Episode.objects.filter(serie_id=serie_id))
        }
        return render(request, 'episodes.html', context=context)
