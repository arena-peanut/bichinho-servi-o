# Generated by Django 2.0.1 on 2018-01-16 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specie',
            old_name='status',
            new_name='specie',
        ),
    ]
