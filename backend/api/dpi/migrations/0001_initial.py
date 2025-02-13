# Generated by Django 5.1.4 on 2025-01-03 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('NSS', models.CharField(max_length=255, unique=True)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('adress', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('mutuelle', models.CharField(blank=True, max_length=255, null=True)),
                ('medecin_traitant', models.ManyToManyField(related_name='patients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dpi',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dpi.patient')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes')),
            ],
        ),
    ]
