# Generated by Django 4.0.5 on 2022-06-01 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=64, verbose_name='Событие')),
                ('desc', models.TextField(blank=True, max_length=512, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SubEventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTypeName', models.CharField(max_length=64, verbose_name='Тип События')),
                ('desc', models.TextField(blank=True, max_length=512, verbose_name='Описание')),
                ('mainType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Конкретное Событие')),
                ('desc', models.TextField(blank=True, max_length=512, verbose_name='Описание')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('totalTime', models.TimeField()),
                ('status', models.IntegerField(choices=[(1, 'Выполнено'), (2, 'Не Выполнено'), (3, 'Запланированно'), (4, 'Отменено'), (5, 'Перенесено')], default=2)),
                ('mainType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.eventtype')),
                ('sybType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.subeventtype')),
            ],
        ),
    ]
