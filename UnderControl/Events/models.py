from django.db import models
from django.db.models import CASCADE


class EventType(models.Model):
    typeName = models.CharField(
        verbose_name='Событие',
        max_length=64,
        blank=False
    )
    desc = models.TextField(
        verbose_name='Описание',
        max_length=512,
        blank=True
    )

    def __str__(self):
        return self.typeName

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class SubEventType(models.Model):
    mainType = models.ForeignKey(EventType, on_delete=CASCADE)
    subTypeName = models.CharField(
        verbose_name='Тип События',
        max_length=64,
        blank=False
    )
    desc = models.TextField(
        verbose_name='Описание',
        max_length=512,
        blank=True
    )

    def __str__(self):
        return self.subTypeName


    class Meta:
        verbose_name = "Тип События"
        verbose_name_plural = "Типы Событий"


class Event(models.Model):
    mainType = models.ForeignKey(EventType, on_delete=CASCADE)
    sybType = models.ForeignKey(SubEventType, on_delete=CASCADE)
    eventName = models.CharField(
        verbose_name='Конкретное Событие',
        max_length=64,
        blank=False
    )
    desc = models.TextField(
        verbose_name='Описание',
        max_length=512,
        blank=True
    )
    start = models.TimeField()
    end = models.TimeField()
    totalTime = models.TimeField(blank=True)
    status = models.IntegerField(choices=[(1, 'Выполнено'),
                                     (2, 'Не Выполнено'),
                                     (3, 'Запланированно'),
                                     (4, 'Отменено'),
                                     (5, 'Перенесено')],
                            default=2,
                            )

    def __str__(self):
        return self.eventName

    def save(self):
        print(self.totalTime)
        super(Event, self).save()
            


    class Meta:
        verbose_name = "Дело"
        verbose_name_plural = "Дела"
