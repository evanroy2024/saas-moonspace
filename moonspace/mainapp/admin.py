from django.contrib import admin
from .models import MoonPlot


@admin.register(MoonPlot)
class MoonPlotAdmin(admin.ModelAdmin):
    list_display = (
        "plot_number",
        "url",
        "buyer_name",
        "receiver_name",
        "design",
        "song",
        "wants_reply",
        "email",
    )

    search_fields = (
        "plot_number",
        "url",
        "buyer_name",
        "receiver_name",
        "email",
        "message",
    )

    list_filter = (
        "design",
        "song",
        "wants_reply",
    )