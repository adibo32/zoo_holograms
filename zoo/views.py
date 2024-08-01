from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Hologram
from .forms import HologramForm

def index(request):
    holograms = Hologram.objects.all()
    return render(request, 'index.html', {'holograms': holograms})

def add_hologram(request):
    if request.method == 'POST':
        form = HologramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HologramForm()
    return render(request, 'add_hologram.html', {'form': form})

def edit_hologram(request, id):
    hologram = get_object_or_404(Hologram, id=id)
    if request.method == 'POST':
        form = HologramForm(request.POST, instance=hologram)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HologramForm(instance=hologram)
    return render(request, 'edit_hologram.html', {'form': form})

def delete_hologram(request, id):
    hologram = get_object_or_404(Hologram, id=id)
    if request.method == 'POST':
        hologram.delete()
        return redirect('index')
    return render(request, 'delete_hologram.html', {'hologram': hologram})
