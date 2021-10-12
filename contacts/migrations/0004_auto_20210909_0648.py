# Generated by Django 3.2.7 on 2021-09-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_contact_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_picture',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_favourite',
            field=models.BooleanField(default=True),
        ),
    ]
