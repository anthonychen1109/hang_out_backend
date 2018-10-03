# Generated by Django 2.0.4 on 2018-10-02 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_group_hometown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organizer_name', to=settings.AUTH_USER_MODEL),
        ),
    ]