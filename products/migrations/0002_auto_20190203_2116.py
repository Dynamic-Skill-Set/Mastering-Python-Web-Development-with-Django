# Generated by Django 2.1.4 on 2019-02-03 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='url',
            new_name='slug',
        ),
    ]
