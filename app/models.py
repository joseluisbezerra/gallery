from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    localizacao = models.CharField(max_length=100)
    data = models.DateField()
    thumbnail = models.ImageField(null=True, blank=True, upload_to='galeria/thumbnail')

    class Meta:
        ordering = ('data',)

    def __str__(self):
        return self.titulo

class Imagem(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(null=True, blank=True, upload_to='galeria/imagens')

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Album)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()