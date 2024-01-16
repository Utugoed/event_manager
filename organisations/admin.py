from django.contrib import admin

from organisations.models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "description", "full_address", )
    list_filter = ("id", )
    search_fields = ("title", )

    def full_address(self, organisation):
        return f"{organisation.address} {organisation.postcode}"
    
admin.site.register(Organisation, OrganisationAdmin)