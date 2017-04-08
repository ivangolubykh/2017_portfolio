from django.db import models
from django.core.urlresolvers import reverse
''' Предусмотрел в БД 4 уровня заголовков, т.к. в перспективе структура
 электронного резюмерезюме может сильно меняться.
'''


class MainHeader1Text(models.Model):
    ''' Текстовые заголовки уровня <h1>
    '''
    # Порядковый номер заголовка в тексте
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
            help_text='Порядковый номер заголовка h1 на странице',
            verbose_name="Порядковый номер заголовка h1 на странице",
                )

    text = models.CharField(max_length=255,
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
                            help_text='Заголовки (h1) для главной страницы',
                            verbose_name="Заголовки (h1) для главной страницы",
                            )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('admin')


class MainHeader2Text(models.Model):
    ''' Текстовые заголовки уровня <h2>
    '''
    # Порядковый номер заголовка в тексте
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
            help_text='Порядковый номер заголовка h2 на странице',
            verbose_name="Порядковый номер заголовка h2 на странице",
                )

    text = models.CharField(max_length=255,
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
                            help_text='Заголовки (h2) для главной страницы',
                            verbose_name="Заголовки (h2) для главной страницы",
                            )

    up = models.ForeignKey(MainHeader1Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('admin')


class MainHeader3Text(models.Model):
    ''' Текстовые заголовки уровня <h3>
    '''
    # Порядковый номер заголовка в тексте
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
            help_text='Порядковый номер заголовка h3 на странице',
            verbose_name="Порядковый номер заголовка h3 на странице",
                )

    text = models.CharField(max_length=255,
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
                            help_text='Заголовки (h3) для главной страницы',
                            verbose_name="Заголовки (h3) для главной страницы",
                            )

    up = models.ForeignKey(MainHeader2Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('admin')


class MainHeader4Text(models.Model):
    ''' Текстовые заголовки уровня <h4>
    '''
    # Порядковый номер заголовка в тексте
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
            help_text='Порядковый номер заголовка h4 на странице',
            verbose_name="Порядковый номер заголовка h4 на странице",
                )

    text = models.CharField(max_length=255,
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
                            help_text='Заголовки (h4) для главной страницы',
                            verbose_name="Заголовки (h4) для главной страницы",
                            )

    up = models.ForeignKey(MainHeader3Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('admin')


class MainText(models.Model):
    ''' Абзацы с текстом на странице
    '''
    # Порядковый номер абзаца в тексте
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
            help_text='Порядковый номер абзаца в тексте',
            verbose_name="Порядковый номер абзаца в тексте",
                )

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
                            help_text='Текст абзаца',
                            verbose_name="Текст абзаца",
                            )

    up = models.ForeignKey(MainHeader4Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('admin')
