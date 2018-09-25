# Generated by Django 2.1.1 on 2018-09-25 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180925_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='tags',
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(default=1, related_name='group_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
