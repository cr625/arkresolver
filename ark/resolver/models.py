from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.deletion import PROTECT
from django.urls import reverse
import uuid


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="PUBLISHED")


class ARK(models.Model):
    id = models.AutoField(primary_key=True)  # change this to ark later
    # the uuid here is temporary and must eventually follow ARK betanumeric convention
    ark_id = models.UUIDField(default=uuid.uuid1)
    shoulder = models.CharField(max_length=10, default="c1")
    # Each orginization should have its own NAAN get one here: https://arks.org/about/getting-started-implementing-arks/
    # TODO: add an option to specify in config
    NAAN_IDS = [
        ("13183", "MRC"),
        ("87918", "Library"),
        ("12345", "example"),
        ("99152", "term"),
        ("99166", "agent"),
        ("99999", "test"),
    ]
    naan = models.CharField(max_length=10, choices=NAAN_IDS, default="MRC")
    target_uri = models.URLField(blank=True, max_length=255)
    archive_uri = models.URLField(blank=True, max_length=255)
    collection = models.CharField(max_length=200, default="Drexel Web")
    title = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, default="User", on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    StatusType = models.TextChoices("Status", "AVAILABLE RESERVED PUBLIC PUBLISHED")
    status = models.CharField(
        default="PUBLISHED", choices=StatusType.choices, max_length=10
    )

    # returns the canonical url for an ark detail entry
    def get_absolute_url(self):
        return reverse("resolver:ark_detail", args=[self.ark_id])

    # when the ark object is called with no arguments returns this string
    def __str__(self):
        trunc_arc = str(self.ark_id)
        trunc_arc = trunc_arc[:8]
        return "ark:/{}/{}{}".format(self.naan, self.shoulder, trunc_arc)

    class Meta:
        ordering = ("naan", "shoulder", "ark_id")
        # all three together should be unique in this context
        constraints = [
            models.UniqueConstraint(
                fields=["naan", "shoulder", "ark_id"], name="unique_ark"
            )
            # condition=Q(status=3)
        ]

    # model managers
    objects = models.Manager()
    published = PublishedManager()


class KernelMetadatum(models.Model):  # https://dublincore.org/groups/kernel/spec/
    id = models.AutoField(primary_key=True)
    ark = models.ForeignKey(ARK, on_delete=models.CASCADE)
    # '', about, meta, support, depositor
    ErcType = models.TextChoices("ErcType", "about meta support depositor")
    erc = models.CharField(blank=True, choices=ErcType.choices, max_length=10)
    who = models.TextField(blank=True)
    what = models.TextField(blank=True)
    when = models.TextField(blank=True)
    where = models.TextField(blank=True)
    how = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "KernelMetadata"


class Capture(models.Model):
    id = models.AutoField(primary_key=True)
    parent_ark = models.ForeignKey(
        ARK, on_delete=models.CASCADE, related_name="capture"
    )
    capture_naan = models.CharField(
        max_length=20, default="13183"
    )  # TODO: inherit this
    capture_shoulder = models.CharField(
        max_length=20, default="c1"
    )  # TODO: inherit this
    capture_ark_id = models.UUIDField(default=uuid.uuid1)
    warc = models.CharField(max_length=200, blank=True)
    manifest = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        trunc_arc = str(self.capture_ark_id)
        trunc_arc = trunc_arc[:8]

        return "ark:/{}/{}{}".format(
            self.capture_naan, self.capture_shoulder, trunc_arc
        )
