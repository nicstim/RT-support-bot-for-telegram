# Generated by Django 3.0.6 on 2020-11-14 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_auto_20201114_0438'),
    ]

    operations = [
        migrations.DeleteModel(
            name='auxiliary_table',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
