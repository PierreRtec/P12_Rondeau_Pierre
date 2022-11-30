from django.contrib import admin

from . import models

admin.site.site_header = "Epic Events Admin"
admin.site.site_title = "Epic Events"

admin.site.register(models.Customer)
admin.site.register(models.Event)
admin.site.register(models.Contract)
