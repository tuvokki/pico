from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Quote


class QuoteResource(resources.ModelResource):

    class Meta:
        model = Quote


class QuoteAdmin(ImportExportModelAdmin):
    resource_class = QuoteResource


admin.site.register(Quote, QuoteAdmin)
