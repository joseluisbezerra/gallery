from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

def album_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.slug, ext)
    # file will be uploaded to MEDIA_ROOT/galeria/thumbnail/<filename>
    return 'galeria/thumbnail/{}'.format(filename)

def imagem_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.titulo, ext)
    # file will be uploaded to MEDIA_ROOT/galeria/imagens/<filename>
    return 'galeria/imagens/{}-{}'.format(instance.album.slug, filename)

class Album(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título do evento')
    descricao = models.TextField(verbose_name='Descrição do evento')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    localizacao = models.CharField(max_length=100, verbose_name='Localização do evento')
    data = models.DateField(verbose_name='Data do evento')
    thumbnail = models.ImageField(null=True, blank=True, upload_to=album_directory_path, verbose_name='Cartaz do evento')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('data',)

    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbuns"


class Imagem(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='A qual álbum se refere')
    titulo = models.CharField(max_length=100, verbose_name='Título da imagem')
    imagem = models.ImageField(null=True, blank=True, upload_to=imagem_directory_path)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

@receiver(post_save, sender=Album)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()