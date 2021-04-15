from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.deletion import PROTECT
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(
            PublishedManager, self
        ).get_queryset()  # .filter(status=3 for published)


class ARK(models.Model):
    id = models.AutoField(primary_key=True)  # change this to ark later
    ark_id = models.CharField(max_length=200, unique=True)
    shoulder = models.CharField(max_length=10, default="a1")
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
    collection = models.CharField(max_length=200, default="Drexel Web")
    title = models.CharField(blank=True, max_length=255)
    notes = models.TextField(blank=True)
    author = models.ForeignKey(User, default="User", on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    format = models.CharField(blank=True, max_length=255)

    class Status(models.IntegerChoices):
        UNAVAILABLE = 0
        RESERVED = 1
        PUBLIC = 2
        PUBLISHED = 3

    status = models.IntegerField(default=0, choices=Status.choices)

    def get_absolute_url(self):
        return reverse(
            "resolver:ark_detail", args=[self.naan, self.shoulder, self.ark_id]
        )

    def __str__(self):
        return "ark:/{}/{}{}".format(self.naan, self.shoulder, self.ark_id)

    class Meta:
        ordering = ("naan", "shoulder", "ark_id")

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
