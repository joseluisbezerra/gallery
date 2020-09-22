from django.contrib import admin

from .models import Album, Imagem

@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'data')
    search_fields = ('titulo',)


@admin.register(Imagem)
class AdminImagem(admin.ModelAdmin):
    list_display = ('titulo', 'album')
    list_filter = ('album',)
    search_fields = ('titulo',)

