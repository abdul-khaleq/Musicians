from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_album(request):
    title = 'Add Abum'
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album_form, 'title':title})

def edit_album(request, id):
    title = 'Edit Abum'
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'add_album.html', {'form': album_form, 'title':title})