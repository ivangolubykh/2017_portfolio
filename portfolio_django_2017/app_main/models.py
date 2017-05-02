from django.db import models
from django.core.urlresolvers import reverse
''' Предусмотрел в БД 4 уровня заголовков или списков, т.к. в
 перспективе структура электронного резюмерезюме может сильно меняться.
'''
from .models_main_page import *
from .models_examples_work_python import *
from .models_examples_work_js import *
from .models_examples_work_html_css import *
from .models_examples_work_education import *


class Weather_For_Json(models.Model):
    ''' Данные погоды за последнее время, чтобы не делать частых запросов
    по api.
    '''
    # Время внесения изменений
    datetime = models.DateTimeField(
        # auto_now = True сделает так, чтобы значение поля автоматически
        # устанавливалось в текущую дату и время при каждом сохранении объекта.
        auto_now=True,
        help_text='Дата и время последнего сохранения данных погоды из api',
        verbose_name="Дата и время последнего сохранения данных погоды из api",
        )

    image = models.CharField(max_length=255,
                             # При blank=True поле может быть пустым
                             # (т.е. оно необязательное):
                             blank=True,
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
                             help_text='Путь к файлу картинки погоды',
                             verbose_name='Путь к файлу картинки погоды',
                             )
    temperature = models.CharField(max_length=10,
                                   # При blank=True поле может быть пустым
                                   # (т.е. оно необязательное):
                                   blank=True,
                                   # Если строковое поле содержит null=True,
                                   # это означает, что оно может содержать два
                                   # возможных “пустых” значения: NULL и
                                   # пустую строку. Иначе - только пустую
                                   # строку.
                                   null=False,
                                   # Строить ли индекс по этому полю:
                                   db_index=False,
                                   # При unique=True значение поля должно быть
                                   # уникальным.
                                   unique=False,
                                   help_text='Температура воздуха',
                                   verbose_name='Температура воздуха',
                                   )
    text = models.CharField(max_length=100,
                            # При blank=True поле может быть пустым
                            # (т.е. оно необязательное):
                            blank=True,
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
                            help_text='Текстовое описание погоды, например:'
                                      ' Солнечно',
                            verbose_name='Текстовое описание погоды, например:'
                                         ' Солнечно',
                            )

    def __str__(self):
        return self.text
