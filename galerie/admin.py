from django.contrib import admin
from galerie.models import Photograph

class ListPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    search_fields = ("name", ) # needs to have more than one 
    list_filter = ("category", ) # needs to have more than one 
    list_editable = ("published", ) # needs to have more than one 
    list_per_page = 10

# All classes must be registered here
admin.site.register(Photograph, ListPhotographs)