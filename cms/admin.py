from django.contrib import admin
from .models import Chara


class CharaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


admin.site.register(Chara, CharaAdmin)
