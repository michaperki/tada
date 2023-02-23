from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Tada



def index(request):
    latest_list = Tada.objects.order_by('-pub_date')[:5]
    context = {'latest_list': latest_list}
    return render(request, 'tada/index.html', context)

def detail(request, tada_id):
    tada = get_object_or_404(Tada, pk=tada_id)
    return render(request, 'tada/detail.html', {'tada': tada})

def results(request, tada_id):
    response = "You're looking at the results of tada %s."
    return HttpResponse(response % tada_id)

def modules(request, tada_id):
    tada = get_object_or_404(Tada, pk=tada_id)
    return render(request, 'tada/modules.html', {'tada': tada})