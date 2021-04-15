# Generated by Django 3.2 on 2021-04-14 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ARK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ark_id', models.CharField(max_length=200, unique=True)),
                ('shoulder', models.CharField(default='a1', max_length=10)),
                ('naan', models.CharField(choices=[('13183', 'MRC'), ('87918', 'Library'), ('12345', 'example'), ('99152', 'term'), ('99166', 'agent'), ('99999', 'test')], default='MRC', max_length=10)),
                ('target_uri', models.URLField(blank=True, max_length=255)),
                ('collection', models.CharField(default='Drexel Web', max_length=200)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('format', models.CharField(blank=True, max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Reserved'), (2, 'Public'), (3, 'Published')], default=0)),
                ('author', models.ForeignKey(default='User', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('naan', 'shoulder', 'ark_id'),
            },
        ),
        migrations.CreateModel(
            name='KernelMetadatum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erc', models.CharField(blank=True, choices=[('about', 'About'), ('meta', 'Meta'), ('support', 'Support'), ('depositor', 'Depositor')], max_length=10)),
                ('who', models.TextField(blank=True)),
                ('what', models.TextField(blank=True)),
                ('when', models.TextField(blank=True)),
                ('where', models.TextField(blank=True)),
                ('how', models.TextField(blank=True)),
                ('ark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resolver.ark')),
            ],
            options={
                'verbose_name_plural': 'KernelMetadata',
            },
        ),
    ]
