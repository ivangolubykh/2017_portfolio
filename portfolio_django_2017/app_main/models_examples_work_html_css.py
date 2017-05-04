from django.db import models
from django.core.urlresolvers import reverse
''' Предусмотрел в БД 4 уровня заголовков или списков, т.к. в
 перспективе структура электронного резюмерезюме может сильно меняться.
'''


# #################
# Группа классов модели для данных страницы примеров работ на HTML/CSS:
# #################
class ExamplesHtmlCssHeaderorList1Text(models.Model):
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
            verbose_name='Порядковый номер заголовка h1 на странице',
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
                            help_text='Заголовки (h1) для страницы',
                            verbose_name='Заголовки (h1) для страницы',
                            )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_html_css')


class ExamplesHtmlCssHeaderorList2Text(models.Model):
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
                            help_text='Заголовки (h2) для страницы',
                            verbose_name="Заголовки (h2) для страницы",
                            )

    up = models.ForeignKey(ExamplesHtmlCssHeaderorList1Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_html_css')


class ExamplesHtmlCssHeaderorList3Text(models.Model):
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
                            help_text='Заголовки (h3) для страницы',
                            verbose_name="Заголовки (h3) для страницы",
                            )

    up = models.ForeignKey(ExamplesHtmlCssHeaderorList2Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_html_css')


class ExamplesHtmlCssHeaderorList4Text(models.Model):
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
                            help_text='Заголовки (h4) для страницы',
                            verbose_name="Заголовки (h4) для страницы",
                            )

    up = models.ForeignKey(ExamplesHtmlCssHeaderorList3Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_html_css')


class ExamplesHtmlCssText(models.Model):
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

    up = models.ForeignKey(ExamplesHtmlCssHeaderorList4Text,
                           # При удаении ключа, удалять и эту запись:
                           on_delete=models.CASCADE,
                           )

    def __str__(self):
        return '{} - {}'.format(self.ordinal, self.text)

    def get_absolute_url(self):
        return reverse('admin_examples_work_html_css')
# #################
# Окончание группы классов модели для страницы примеров работ на HTML/CSS.
# #################
