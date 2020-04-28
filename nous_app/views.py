from django.shortcuts import render
from .forms import ItemFrom

# Create your views here.


def items_list(request):
    return render(request, 'nous_app/items_list.html')


def items_add(request):
    form = ItemFrom()
    return render(request, 'nous_app/items_add.html', {'form': form})


def items_delete(request):
    return