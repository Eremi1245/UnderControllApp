# Generated by Django 4.0.5 on 2022-06-01 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_alter_eventtype_options_rename_name_event_eventname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Дело', 'verbose_name_plural': 'Дела'},
        ),
        migrations.AlterModelOptions(
            name='subeventtype',
            options={'verbose_name': 'Тип События', 'verbose_name_plural': 'Типы Событий'},
        ),
    ]
