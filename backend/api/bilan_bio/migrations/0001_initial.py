

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
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('descirption', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BilanBiologique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('satisfait', models.BooleanField(default=False)),
                ('date', models.DateField(default=None)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation')),
                ('laborantient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biological_tests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParamValeur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valeur', models.FloatField()),
                ('unite', models.CharField(max_length=255)),
                ('parametre', models.CharField(max_length=255)),
                ('bilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilan_bio.bilanbiologique')),
            ],
        ),
    ]
