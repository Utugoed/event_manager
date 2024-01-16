from django.contrib import admin
from django.utils.html import format_html

from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "get_thumbnail", "id", "description", "organisations_list", "image", "date", )
    list_filter = ("id", "date", )
    search_fields = ("title",)
    readonly_fields = ("get_thumbnail", )

    def organisations_list(self, event):
        return ', '.join([organisation.title for organisation in event.organisations.all()])
    
    def get_thumbnail(self, event):
        if (event.image):
            return format_html(f'<img src="{event.image.url}" width="150" height="150" />')
        return "No Image"

    get_thumbnail.short_description = "Thumbnail"

admin.site.register(Event, EventAdmin)