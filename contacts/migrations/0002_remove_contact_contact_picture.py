# Generated by Django 3.2.7 on 2021-09-08 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_picture',
        ),
    ]
