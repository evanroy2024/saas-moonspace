from django.db import models
import uuid


class MoonPlot(models.Model):
    buyer_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="moon_plots/", blank=True, null=True)

    message = models.TextField(blank=True)

    plot_number = models.CharField(
        max_length=30,
        unique=True,
        editable=False
    )

    url = models.CharField(
        max_length=12,
        unique=True,
        editable=False
    )

    song = models.PositiveSmallIntegerField(
        choices=[(i, f"Song {i}") for i in range(1, 21)]
    )

    design = models.PositiveSmallIntegerField(
        choices=[(i, f"Design {i}") for i in range(1, 6)],
        default=1
    )

    wants_reply = models.BooleanField(default=False)
    email = models.EmailField(blank=True)

    def save(self, *args, **kwargs):
        if not self.plot_number:
            self.plot_number = f"LUNA-{uuid.uuid4().hex[:8].upper()}"

        if not self.url:
            self.url = uuid.uuid4().hex[:8]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.plot_number