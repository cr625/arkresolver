# Generated by Django 3.1.7 on 2021-04-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ark',
            name='format',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='ark',
            name='naan',
            field=models.CharField(choices=[('13183', 'MRC'), ('87918', 'Library'), ('12345', 'example'), ('99152', 'term'), ('99166', 'agent'), ('99999', 'test')], default='MRC', max_length=10),
        ),
    ]
