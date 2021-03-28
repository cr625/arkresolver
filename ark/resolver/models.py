from django.db import models

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
    naan = models.CharField(default='99152', max_length=10, choices=NAAN_IDS)
