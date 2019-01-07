# Generated by Django 2.1.2 on 2018-12-14 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_place_abbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileageuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mileage_user', to=settings.AUTH_USER_MODEL),
        ),
    ]