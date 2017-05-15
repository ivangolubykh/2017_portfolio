from django.db import models
from django.core.urlresolvers import reverse
''' Предусмотрел в БД 4 уровня заголовков или списков, т.к. в
 перспективе структура электронного резюмерезюме может сильно меняться.
'''


# #################
# Группа классов модели для данных страницы примеров работ на питоне:
# #################
class ExamplesPython(models.Model):
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

    # Название проекта:
    name_project = models.CharField(
        max_length=255,
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
        help_text='Название проекта',
        verbose_name='Название проекта',
        )

    # Картинка проекта, если есть.
    image = models.ImageField(
        # Куда загружать эти картинки:
        upload_to='examples_python_images/',
        # При blank=True поле может быть пустым
        # (т.е. оно необязательное):
        blank=True,
        verbose_name="Картинка проекта")

    # Ссылка на проект в сети:
    net_address = models.CharField(
        max_length=255,
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
        help_text='Ссылка на проект в сети',
        verbose_name='Ссылка на проект в сети',
        )

    # Ссылка на git-репозиторий проекта:
    git_address = models.CharField(
        max_length=255,
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
        help_text='Ссылка на git-репозиторий проекта',
        verbose_name='Ссылка на git-репозиторий проекта',
        )

    # Описание проекта:
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
        help_text='Описание проекта',
        verbose_name='Описание проекта',
        )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_python')

    def delete(self, *args, **kwargs):
        # До удаления записи получаем необходимую информацию
        storage, filepath = self.image.storage, self.image.path
        # Удаляем сначала модель ( объект )
        super(__class__, self).delete(*args, **kwargs)
        # Потом удаляем сам файл
        storage.delete(filepath)
# #################
# Окончание группы классов модели для страницы примеров работ на питоне.
# #################
