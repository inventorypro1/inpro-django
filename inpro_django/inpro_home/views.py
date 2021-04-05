from django.shortcuts import render
from django.views.generic import (
    DetailView,
)
from .models import Locker, ItemType, Item


def home(request):
    context = {
        'lockers': Locker.objects.all(),
        'itemTypes': ItemType.objects.all()
    }
    return render(request, 'inpro_home/home.html', context)


class LockerDetailView(DetailView):
    model = Locker

    def get_context_data(self, **kwargs):
        context = super(LockerDetailView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(locker=self.object)
        return context
