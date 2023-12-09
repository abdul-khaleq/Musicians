from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    title = 'Add Musician'
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form, 'title': title})

def delete_album(request, id):
    print(id)
    album = models.Musician.objects.get(pk=id).delete()
    return redirect('homepage')

def edit_musician(request, id):
    title = 'Edit Musician'
    print(id)
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html', {'form': musician_form, 'title': title})
