# Generated by Django 3.2.5 on 2021-07-25 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='reason',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]