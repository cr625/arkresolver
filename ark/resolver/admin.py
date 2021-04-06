from django.contrib import admin
from .models import ARK


@admin.register(ARK)
class ARKAdmin(admin.ModelAdmin):
    list_display = ('naan', 'ark_id', 'collection',
                    'title', 'author', 'created')
    list_filter = ('naan', 'status', 'collection', 'created')
    search_fields = ('title', 'ark_id')
    #raw_id_fields = ('collection')
    ordering = ('naan', 'ark_id')
