from django.db import models


class Adjective(models.Model):
    text = models.CharField('Введите прилагательное', max_length=60)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Прилагательное'
        verbose_name_plural = 'Прилагательные'
