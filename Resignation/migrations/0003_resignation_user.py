# Generated by Django 4.0.1 on 2022-01-10 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Resignation', '0002_rename_prim_reason_resignation_reason_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resignation',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
