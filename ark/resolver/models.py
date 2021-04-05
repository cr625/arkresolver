from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.deletion import PROTECT


class ARK(models.Model):
    ark_id = models.CharField(max_length=200, unique=True)
    shoulder = models.CharField(max_length=10, default='a1')
    NAAN_IDS = [
        ('13183', 'MRC'),
        ('87918', 'Library'),
        ('12345', 'example'),
        ('99152', 'term'),
        ('99166', 'agent'),
        ('99999', 'test'),
    ]
    naan = models.CharField(max_length=10, choices=NAAN_IDS, default='MRC')
    target_uri = models.URLField(blank=True, max_length=255)
    collection = models.CharField(max_length=200, default='Drexel Web')
    title = models.CharField(blank=True, max_length=255)
    notes = models.TextField(blank=True)
    author = models.ForeignKey(User, default='User', on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    format = models.CharField(blank=True, max_length=255)

    class Status(models.IntegerChoices):
        UNAVAILABLE = 0
        RESERVED = 1
        PUBLIC = 2
        PUBLISHED = 3

    status = models.IntegerField(default=0, choices=Status.choices)

    def __str__(self):
        return 'ark:/{}/{}{}'.format(self.naan, self.shoulder, self.ark_id)

    class Meta:
        ordering = ('naan', 'shoulder', 'ark_id')


class KernelMetadatum(models.Model):  # https://dublincore.org/groups/kernel/spec/
    ark = models.ForeignKey(ARK, on_delete=models.CASCADE)
    # '', about, meta, support, depositor
    ErcType = models.TextChoices(
        'ErcType', 'about meta support depositor')
    erc = models.CharField(blank=True, choices=ErcType.choices, max_length=10)
    who = models.TextField(blank=True)
    what = models.TextField(blank=True)
    when = models.TextField(blank=True)
    where = models.TextField(blank=True)
    how = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'KernelMetadata'
