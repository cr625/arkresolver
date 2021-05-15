from django.contrib import admin
from .models import ARK, KernelMetadatum, Capture


@admin.register(ARK)
class ARKAdmin(admin.ModelAdmin):
    list_display = ("ark_id", "naan", "collection", "title", "author", "created")
    list_filter = ("naan", "status", "collection", "created")
    search_fields = ("naan", "title", "ark_id")
    # raw_id_fields = ('collection')
    ordering = ("naan", "ark_id")


@admin.register(Capture)
class CaptureAdmin(admin.ModelAdmin):
    list_display = ("capture_ark_id", "capture_uri", "warc", "manifest", "created")

@admin.register(KernelMetadatum)
class KernelMetadatumAdmin(admin.ModelAdmin):
    ordering = ("ark",)