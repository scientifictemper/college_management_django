# Generated by Django 3.2.5 on 2021-07-26 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clg', '0002_permission_reason'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='address',
            new_name='department',
        ),
    ]
