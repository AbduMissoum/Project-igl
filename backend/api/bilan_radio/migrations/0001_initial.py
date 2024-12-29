

import bilan_radio.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('consultation', '0001_initial'),

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BilanRadiologique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('compte_rendu', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=255)),
                ('satisfait', models.BooleanField(default=False)),

                ('date', models.DateField(default=None)),

                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation')),
                ('radiologe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenImagerieMedicale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('examen_image', models.ImageField(blank=True, null=True, upload_to=bilan_radio.models.upload_to)),
                ('bilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilan_radio.bilanradiologique')),
            ],
        ),
    ]
