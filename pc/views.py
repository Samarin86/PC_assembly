from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Computer


def index(request):
    computers = Computer.objects.all()
    return render(request, 'index.html', {'computers': computers})

def single_computer(request, computer_id):
    try:
        computer = Computer.objects.get(pk=computer_id)
        return render(request, 'single_computer.html', {'computer': computer})
    except Computer.DoesNotExist:
        raise Http404()