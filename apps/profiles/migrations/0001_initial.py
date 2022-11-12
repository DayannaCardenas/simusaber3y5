# Generated by Django 2.2.14 on 2022-10-18 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeVerify',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('code', models.CharField(max_length=6)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='states.State')),
            ],
        ),
    ]
