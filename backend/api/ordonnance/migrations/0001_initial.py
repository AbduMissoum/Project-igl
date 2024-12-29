

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('la_dose', models.CharField(max_length=255)),
                ('la_durre', models.CharField(blank=True, max_length=255, null=True)),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordonnance.medicament')),
                ('ordonnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordonnance.ordonnance')),
            ],
        ),
    ]
