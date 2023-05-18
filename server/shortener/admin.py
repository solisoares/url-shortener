from django.contrib import admin

from shortener.models import URL


class URLAdmin(admin.ModelAdmin):
    readonly_fields = (
        "original_url",
        "short_url",
        "creation_datetime",
        "last_access_datetime",
        "access_count",
    )


admin.site.register(URL, URLAdmin)
