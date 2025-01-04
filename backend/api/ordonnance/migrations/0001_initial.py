# Generated by Django 5.1.4 on 2025-01-04 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valide', models.BooleanField(default=False)),
                ('consultation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('la_dose', models.CharField(max_length=255)),
                ('la_durre', models.CharField(blank=True, max_length=255, null=True)),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordonnance.medicament')),
                ('ordonnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traitements', to='ordonnance.ordonnance')),
            ],
        ),
    ]
