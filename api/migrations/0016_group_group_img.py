# Generated by Django 2.1.1 on 2018-09-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20180926_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_img',
            field=models.TextField(default=''),
        ),
    ]
