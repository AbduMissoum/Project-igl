# Generated by Django 5.1.4 on 2024-12-29 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
        ('ordonnance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordonnance',
            name='consultation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation'),
        ),
    ]
