# Generated by Django 2.1.1 on 2018-09-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180921_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(to='api.UserProfile'),
        ),
    ]
