from django.contrib import admin
from imagekit.admin import AdminThumbnail

# Register your models here.

from models import *

class ImagesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image',           {'fields':  ['title', 'author', 'original_img']}),
        ('Description',     {'fields':  ['creation_date', 'country']}),
        ('Specification',   {'fields':  ['style', 'main_colour', 'pub_date']}),
    ]
    list_display = ('title', 'author', 'pub_date', 'creation_date', 'preview', 'was_published_recently')
    preview = AdminThumbnail(image_field='admin_block_img')
    search_fields = ('title',)
    list_filter = ['pub_date']


class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['last_name', 'first_name']}),
        ('Contacts',        {'fields': ['email'], 'classes': ['collapse']}),
        ('With us from',    {'fields': ['with_us']}),
    ]
    list_display = ('last_name', 'first_name', 'email', 'with_us')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('with_us',)

admin.site.register(Author, AuthorsAdmin)
admin.site.register(Image, ImagesAdmin)