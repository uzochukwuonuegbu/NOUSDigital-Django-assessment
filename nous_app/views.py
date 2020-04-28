from django.shortcuts import render, redirect
from .forms import ItemFrom
from .models import Item

# Create your views here.


def items_list(request):
    context = {'items_list': Item.objects.all()}
    return render(request, 'nous_app/items_list.html', context)


def items_add(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ItemFrom()
        else:
            item = Item.objects.get(pk=id)
            form = ItemFrom(instance=item)
        return render(request, 'nous_app/items_add.html', {'form': form})

    elif request.method == "POST":
        if id == 0:
            form = ItemFrom(request.POST)
        else:
            item = Item.objects.get(pk=id)
            form = ItemFrom(request.POST, instance=item)
        if form.is_valid():
            form.save()
        
        return redirect('/items/list')

def items_delete(request, id=0):
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect('/items/list')