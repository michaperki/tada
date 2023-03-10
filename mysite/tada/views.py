from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Tada, Module, Setting

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

def module(request, tada_id, module_id):
    tada = get_object_or_404(Tada, pk=tada_id)
    module = get_object_or_404(Module, pk=module_id)
    return render(request, 'tada/module.html', {'tada': tada, 'module': module})

def setting(request, tada_id, setting_id=None):
    tada = get_object_or_404(Tada, pk=tada_id)
    if setting_id:
        setting = get_object_or_404(Setting, pk=setting_id)
        return render(request, 'tada/setting.html', {'tada': tada, 'setting': setting})
    else:
        return render(request, 'tada/setting.html', {'tada': tada})