import random
import string
from io import BytesIO
from os.path import exists
from PIL import Image
from django.test import TestCase
from django.db import transaction
from django.core.urlresolvers import reverse
from django.core.files import File
from django.conf import settings
from . import factories

__author__ = 'Иван Голубых'


class BaseTest(TestCase):
    def assertEqualModelFields(self, obj, model_fields):
        """
            asserts django model object fields & test case object attr

            :param model_fields: django model fields
            :type model_fields: iterable
            :param obj: django model object
            :type obj: Django Model
        """
        for field in model_fields:
            self.assertEqual(getattr(obj, field), getattr(self, field))

    @staticmethod
    def get_image_file(
            name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)
    ):
        """ create image file for django image field """
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)


class Weather_For_JsonModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.Weather_For_JsonFactory._meta.model
        self.object = factories.Weather_For_JsonFactory.create()

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.Weather_For_Json model initials """
        self.assertIsNotNone(self.object.datetime)
        self.assertEquals(self.object.image, '')
        self.assertEquals(self.object.temperature, '')
        self.assertEquals(self.object.text, '')

    @transaction.atomic()
    def test_str_method(self):
        """ Testing app_main.Weather_For_Json model __str__ method """
        self.assertEqual('{}'.format(self.object), '')

        _text = ''.join(random.choice(string.printable) for _ in range(300))
        _object = factories.Weather_For_JsonFactory.create(text=_text)
        self.assertEqual('{}'.format(_object), _text)
        _object.delete()


# #################
# Группа классов модели для данных главной страницы (models_main_page):
# #################
class MainHeader1TextModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.MainHeader1TextFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.object = factories.MainHeader1TextFactory.create(
            ordinal=self.ordinal
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.MainHeader1Text model initials """
        fields = ('ordinal',)
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(self.object.text, '')

    def test_str_method(self):
        """ Testing app_main.MainHeader1Text model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - '.format(self.ordinal))

    def test_get_absolute_url_method(self):
        """ Testing app_main.MainHeader1Text model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(), reverse('admin'))


class MainHeader2TextModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.MainHeader2TextFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.up = factories.MainHeader1TextFactory.create()
        self.object = factories.MainHeader2TextFactory.create(
            ordinal=self.ordinal, up=self.up
        )

    def tearDown(self):
        self.object.delete()
        self.up.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.MainHeader2Text model initials """
        fields = ('ordinal', 'up')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(self.object.text, '')

    def test_str_method(self):
        """ Testing app_main.MainHeader2Text model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - '.format(self.ordinal))

    def test_get_absolute_url_method(self):
        """ Testing app_main.MainHeader2Text model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(), reverse('admin'))


class MainHeader3TextModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.MainHeader3TextFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.up = factories.MainHeader2TextFactory.create()
        self.object = factories.MainHeader3TextFactory.create(
            ordinal=self.ordinal, up=self.up
        )

    def tearDown(self):
        self.object.delete()
        self.up.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.MainHeader3Text model initials """
        fields = ('ordinal', 'up')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(self.object.text, '')

    def test_str_method(self):
        """ Testing app_main.MainHeader3Text model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - '.format(self.ordinal))

    def test_get_absolute_url_method(self):
        """ Testing app_main.MainHeader3Text model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(), reverse('admin'))


class MainHeader4TextModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.MainHeader4TextFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.up = factories.MainHeader3TextFactory.create()
        self.object = factories.MainHeader4TextFactory.create(
            ordinal=self.ordinal, up=self.up
        )

    def tearDown(self):
        self.object.delete()
        self.up.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.MainHeader4Text model initials """
        fields = ('ordinal', 'up')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(self.object.text, '')

    def test_str_method(self):
        """ Testing app_main.MainHeader4Text model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - '.format(self.ordinal))

    def test_get_absolute_url_method(self):
        """ Testing app_main.MainHeader4Text model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(), reverse('admin'))


class MainTextModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.MainTextFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.up = factories.MainHeader4TextFactory.create()
        self.object = factories.MainTextFactory.create(
            ordinal=self.ordinal, up=self.up
        )

    def tearDown(self):
        self.object.delete()
        self.up.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.MainText model initials """
        fields = ('ordinal', 'up')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(self.object.text, '')

    def test_str_method(self):
        """ Testing app_main.MainText model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - '.format(self.ordinal))

    def test_get_absolute_url_method(self):
        """ Testing app_main.MainText model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(), reverse('admin'))


# #################
# Группа классов модели для данных страницы
# примеров работ (models_examples_work_python):
# #################
class ExamplesPythonModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.ExamplesPythonFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.name_project = ''.join(random.choice(string.printable)
                                    for _ in range(255))
        self.text = ''.join(random.choice(string.printable)
                            for _ in range(300))
        self.object = factories.ExamplesPythonFactory.create(
            ordinal=self.ordinal,
            name_project=self.name_project,
            text=self.text,
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.ExamplesPython model initials """
        fields = ('ordinal', 'name_project', 'text')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(str(self.object.image_file), '')
        self.assertEquals(self.object.net_address, '')
        self.assertEquals(self.object.git_address, '')

    def test_str_method(self):
        """ Testing app_main.ExamplesPython model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - {}'.format(self.ordinal, self.text))

    def test_get_absolute_url_method(self):
        """ Testing app_main.ExamplesPython model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(),
                             reverse('admin_examples_work_python'))

    @transaction.atomic()
    def test_delete_method(self):
        """ Testing app_main.ExamplesPython model delete method """
        _image_file = self.get_image_file()
        _object = factories.ExamplesPythonFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file,
        )
        _filepath = _object.image_file.path
        if not exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        _object.delete()
        if exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не удалился с диска при удалении модели'
            )

    @transaction.atomic()
    def test_save_method(self):
        """ Testing app_main.ExamplesPython model save method """
        _image_file1 = self.get_image_file(size=(300, 485))
        _object = factories.ExamplesPythonFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file1,
        )
        _object.refresh_from_db()
        _filepath1 = _object.image_file.path
        if not exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        self.assertEqual(_object.image_file.width, 177)
        self.assertEqual(_object.image_file.height, 286)

        _image_file2 = self.get_image_file()
        _object.image_file = _image_file2
        _object.save()
        _filepath2 = _object.image_file.path
        if exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )
        if not exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - новый файл не создался при сохранении'
            )

        _object.image_file = None
        _object.save()
        if exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )

        _object.delete()


# #################
# Группа классов модели для данных страницы примеров
# работ на JavaScript (models_examples_work_js):
# #################
class ExamplesJsModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.ExamplesJsFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.name_project = ''.join(random.choice(string.printable)
                                    for _ in range(255))
        self.text = ''.join(random.choice(string.printable)
                            for _ in range(300))
        self.object = factories.ExamplesJsFactory.create(
            ordinal=self.ordinal,
            name_project=self.name_project,
            text=self.text,
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.ExamplesJs model initials """
        fields = ('ordinal', 'name_project', 'text')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(str(self.object.image_file), '')
        self.assertEquals(self.object.net_address, '')
        self.assertEquals(self.object.git_address, '')

    def test_str_method(self):
        """ Testing app_main.ExamplesJs model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - {}'.format(self.ordinal, self.text))

    def test_get_absolute_url_method(self):
        """ Testing app_main.ExamplesJs model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(),
                             reverse('admin_examples_work_js'))

    @transaction.atomic()
    def test_delete_method(self):
        """ Testing app_main.ExamplesJs model delete method """
        _image_file = self.get_image_file()
        _object = factories.ExamplesJsFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file,
        )
        _filepath = _object.image_file.path
        if not exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        _object.delete()
        if exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не удалился с диска при удалении модели'
            )

    @transaction.atomic()
    def test_save_method(self):
        """ Testing app_main.ExamplesJs model save method """
        _image_file1 = self.get_image_file(size=(300, 485))
        _object = factories.ExamplesJsFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file1,
        )
        _object.refresh_from_db()
        _filepath1 = _object.image_file.path
        if not exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        self.assertEqual(_object.image_file.width, 177)
        self.assertEqual(_object.image_file.height, 286)

        _image_file2 = self.get_image_file()
        _object.image_file = _image_file2
        _object.save()
        _filepath2 = _object.image_file.path
        if exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )
        if not exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - новый файл не создался при сохранении'
            )

        _object.image_file = None
        _object.save()
        if exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )

        _object.delete()


# #################
# Группа классов модели для данных страницы примеров
# работ на Html/Css (models_examples_work_html_css):
# #################
class ExamplesHtmlCssModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.ExamplesHtmlCssFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.name_project = ''.join(random.choice(string.printable)
                                    for _ in range(255))
        self.text = ''.join(random.choice(string.printable)
                            for _ in range(300))
        self.object = factories.ExamplesHtmlCssFactory.create(
            ordinal=self.ordinal,
            name_project=self.name_project,
            text=self.text,
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.ExamplesHtmlCss model initials """
        fields = ('ordinal', 'name_project', 'text')
        self.assertEqualModelFields(self.object, fields)
        self.assertEquals(str(self.object.image_file), '')
        self.assertEquals(self.object.net_address, '')
        self.assertEquals(self.object.git_address, '')

    def test_str_method(self):
        """ Testing app_main.ExamplesHtmlCss model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - {}'.format(self.ordinal, self.text))

    def test_get_absolute_url_method(self):
        """ Testing app_main.ExamplesHtmlCss model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(),
                             reverse('admin_examples_work_html_css'))

    @transaction.atomic()
    def test_delete_method(self):
        """ Testing app_main.ExamplesHtmlCss model delete method """
        _image_file = self.get_image_file()
        _object = factories.ExamplesHtmlCssFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file,
        )
        _filepath = _object.image_file.path
        if not exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        _object.delete()
        if exists(_filepath):
            self.assertEqual(
                0,
                'Ошибка теста - файл не удалился с диска при удалении модели'
            )

    @transaction.atomic()
    def test_save_method(self):
        """ Testing app_main.ExamplesHtmlCss model save method """
        _image_file1 = self.get_image_file(size=(300, 485))
        _object = factories.ExamplesHtmlCssFactory.create(
            ordinal='108',
            name_project='Test Name Project',
            text=self.text,
            image_file=_image_file1,
        )
        _object.refresh_from_db()
        _filepath1 = _object.image_file.path
        if not exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - файл не создался при сохранении'
            )
        self.assertEqual(_object.image_file.width, 177)
        self.assertEqual(_object.image_file.height, 286)

        _image_file2 = self.get_image_file()
        _object.image_file = _image_file2
        _object.save()
        _filepath2 = _object.image_file.path
        if exists(_filepath1):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )
        if not exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - новый файл не создался при сохранении'
            )

        _object.image_file = None
        _object.save()
        if exists(_filepath2):
            self.assertEqual(
                0,
                'Ошибка теста - старый файл не удалился при сохранении'
            )

        _object.delete()


# #################
# Группа классов модели для данных страницы Учёбы (образование):
# #################
class EducationModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.EducationFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.text = ''.join(random.choice(string.printable)
                            for _ in range(300))
        self.object = factories.EducationFactory.create(
            ordinal=self.ordinal,
            text=self.text,
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.Education model initials """
        fields = ('ordinal', 'text')
        self.assertEqualModelFields(self.object, fields)

    def test_str_method(self):
        """ Testing app_main.Education model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - {}'.format(self.ordinal, self.text))

    def test_get_absolute_url_method(self):
        """ Testing app_main.Education model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(),
                             reverse('admin_education'))


# #################
# Группа классов модели для данных страницы Работы (места работ):
# #################
class WorksModelTest(BaseTest):
    def setUp(self):
        self.obj_model = factories.WorksFactory._meta.model
        self.ordinal = random.randint(0, 10000)
        self.text = ''.join(random.choice(string.printable)
                            for _ in range(300))
        self.object = factories.WorksFactory.create(
            ordinal=self.ordinal,
            text=self.text,
        )

    def tearDown(self):
        self.object.delete()
        self.assertEqual(self.obj_model.objects.count(), 0)

    def test_initials(self):
        """ Testing app_main.Works model initials """
        fields = ('ordinal', 'text')
        self.assertEqualModelFields(self.object, fields)

    def test_str_method(self):
        """ Testing app_main.Works model __str__ method """
        self.assertEqual('{}'.format(self.object),
                         '{} - {}'.format(self.ordinal, self.text))

    def test_get_absolute_url_method(self):
        """ Testing app_main.Works model get_absolute_url method """
        if settings.DEBUG:
            self.assertEqual(self.object.get_absolute_url(),
                             reverse('admin_works'))
