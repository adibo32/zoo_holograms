from django.shortcuts import render, get_object_or_404, redirect
from .models import Hologram
from .forms import HologramForm
from django.contrib import messages

def index(request):
    filter_term = request.GET.get('filter', '')
    sort_column = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')

    if filter_term:
        holograms = Hologram.objects.filter(name__icontains=filter_term)
    else:
        holograms = Hologram.objects.all()

    if sort_order == 'asc':
        holograms = holograms.order_by(sort_column)
    else:
        holograms = holograms.order_by(f'-{sort_column}')

    return render(request, 'index.html', {'holograms': holograms, 'filter_term': filter_term, 'sort_column': sort_column, 'sort_order': sort_order})

def add_hologram(request):
    if request.method == 'POST':
        form = HologramForm(request.POST)
        if form.is_valid():
            hologram = form.save()
            messages.success(request, f'Das Hologramm "{hologram.name}" wurde erfolgreich hinzugefügt.')
            return redirect('index')
    else:
        form = HologramForm()
    return render(request, 'add_hologram.html', {'form': form})

def edit_hologram(request, id):
    hologram = get_object_or_404(Hologram, id=id)
    if request.method == 'POST':
        form = HologramForm(request.POST, instance=hologram)
        if form.is_valid():
            hologram = form.save()
            messages.success(request, f'Die Änderungen im "{hologram.name}" wurden erfolgreich gespeichert.')
            return redirect('index')
    else:
        form = HologramForm(instance=hologram)
    return render(request, 'edit_hologram.html', {'form': form})

def delete_hologram(request, id):
    hologram = get_object_or_404(Hologram, id=id)
    if request.method == 'POST':
        hologram.delete()
        messages.success(request, f'Das Hologramm "{hologram.name}" wurde erfolgreich gelöscht.')
        return redirect('index')
    return render(request, 'delete_hologram.html', {'hologram': hologram})
