# Generated by Django 4.0.5 on 2022-06-01 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventtype',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='eventName',
        ),
    ]