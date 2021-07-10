from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Album, Imagem


class Home(ListView):
    model = Album
    paginate_by = 6
    template_name = 'app/home.html'


def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug)
    imagens = Imagem.objects.filter(album=album)

    return render(request, 'app/album_detail.html', {'album': album, 'imagens': imagens})
