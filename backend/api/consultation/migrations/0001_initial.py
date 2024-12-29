

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('dpi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resume', models.TextField(blank=True, null=True)),
                ('la_date', models.DateField(blank=True, null=True)),
                ('dpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpi.dpi')),
                ('etablisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.etablisement')),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
