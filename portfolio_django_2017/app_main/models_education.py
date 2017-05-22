from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image


# #################
# Группа классов модели для данных страницы Учёбы (образование):
# #################
class Education(models.Model):
    ''' Текстовые заголовки уровня <h1>
    '''
    # Порядковый номер объекта на странице:
    ordinal = models.PositiveSmallIntegerField(
        # При blank=True поле может быть пустым
        # (т.е. оно необязательное):
        blank=False,
        # Если строковое поле содержит null=True, это
        # означает, что оно может содержать два возможных
        # “пустых” значения: NULL и пустую строку.
        # Иначе - только пустую строку.
        null=False,
        # Строить ли индекс по этому полю:
        db_index=True,
        # При unique=True значение поля должно быть
        # уникальным.
        unique=True,
        help_text='Порядковый номер объекта на странице',
        verbose_name='Порядковый номер объекта на странице',
        )

    # Описание места учёбы:
    text = models.TextField(
        # При blank=True поле может быть пустым
        # (т.е. оно необязательное):
        blank=False,
        # Если строковое поле содержит null=True, это
        # означает, что оно может содержать два возможных
        # “пустых” значения: NULL и пустую строку.
        # Иначе - только пустую строку.
        null=False,
        # Строить ли индекс по этому полю:
        db_index=False,
        # При unique=True значение поля должно быть
        # уникальным.
        unique=False,
        help_text='Описание места учёбы',
        verbose_name='Описание места учёбы',
        )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_education')
# #################
# Окончание группы классов модели для страницы Учёбы (образование).
# #################
