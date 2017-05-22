from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image


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
    image_file = models.ImageField(
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
        if self.image_file:
            # До удаления записи получаем необходимую информацию
            storage, filepath = self.image_file.storage, self.image_file.path
            # Потом удаляем сам файл
            storage.delete(filepath)
        # Удаляем запись в БД (объект)
        super(__class__, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Максимальный размер изображения по большей стороне
        _MAX_SIZE = 286
        # Проверяю, есть ли в БД уже этот объект (радактируем старое или
        # создаём новое?):
        old_obj = False
        try:
            old_obj = __class__.objects.get(pk=self.pk)
        except Exception:
            pass
        # Сначала - обычное сохранение
        super(__class__, self).save(*args, **kwargs)
        if old_obj and old_obj.image_file\
                and ((not self.image_file) or
                     (old_obj.image_file.path != self.image_file.path)
                     ):
            # удаляю старый файл, если он был стёрт или обновлён на новый:
            storage = old_obj.image_file.storage
            filepath = old_obj.image_file.path
            storage.delete(filepath)
        # Если добавиласть новая картинка или изменилась старая, то создаю
        # уменьшенную копию:
        if self.image_file\
                and (not old_obj or
                     not old_obj.image_file or
                     (old_obj.image_file and
                      old_obj.image_file.path != self.image_file.path
                      )
                     ):
            filepath = self.image_file.path
            width = self.image_file.width
            height = self.image_file.height
            max_size = max(width, height)
            image_file = Image.open(filepath)
            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image_file = image_file.\
                    resize((round(width / max_size * _MAX_SIZE),
                            round(height / max_size * _MAX_SIZE)),
                           Image.ANTIALIAS
                           )
            # И не забыть сохраниться
                image_file.save(filepath)
# #################
# Окончание группы классов модели для страницы примеров работ на питоне.
# #################
