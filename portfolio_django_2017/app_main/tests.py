import datetime
import mock
from django.test import TestCase
from django.db import transaction
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Weather_For_Json

__author__ = 'Иван Голубых'


class TestMainPage(TestCase):
    fixtures = ['startdata.json']

    def test_main_page(self):
        """ Тест на доступность главной страницы сайта
        """
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200,
                         msg='Главная страница работает неверно:'
                             ' не возвращает код 200 OK')

    def test_main_page_fio(self):
        """ Тест на наличие обязательного текста из БД на главной странице
        сайта.
        """
        response = self.client.get(reverse('main'))
        self.assertIn('Иван Голубых', response.content.decode(),
                      msg='На странице отсутствуют мои ФИО')

    def test_main_page_menu(self):
        """ Тест на наличие всех пунктов меню на сайте: Главная, Примеры работ,
        Учёбы, Работы, Контакты.
        """
        for month in range(1, 13):
            _test_time = datetime.datetime(
                year=2017, month=month, day=16, hour=18, minute=15,
                tzinfo=datetime.timezone.utc
            )
            with mock.patch('django.utils.timezone.now') as perm_mock:
                perm_mock.return_value = _test_time

                response = self.client.get(reverse('main'))
                self.assertIn('>Главная</a>', response.content.decode(),
                              msg='На странице отсутствует меню Главная')
                self.assertIn('>Примеры работ</a>', response.content.decode(),
                              msg='На странице отсутствует меню Примеры работ')
                self.assertIn('>Учёбы</a>', response.content.decode(),
                              msg='На странице отсутствует меню Учёбы')
                self.assertIn('>Работы</a>', response.content.decode(),
                              msg='На странице отсутствует меню Работы')
                self.assertIn('>Контакты</a>', response.content.decode(),
                              msg='На странице отсутствует меню Контакты')

    def test_main_page_futer(self):
        """ Тест на наличие всех обязательных текстов в футере:
        8-921-355-04-60, ivan9@allworld.xyz, kreoya, Иван Борисович Голубых,
        Все права защищены.
        """
        response = self.client.get(reverse('main'))
        self.assertIn('8-921-355-04-60', response.content.decode(),
                      msg='На странице отсутствует мой номер телефона')
        self.assertIn('>ivan9@allworld.xyz</a>', response.content.decode(),
                      msg='На странице отсутствует моя почта')
        self.assertIn('>kreoya</a>', response.content.decode(),
                      msg='На странице отсутствует мой скайп')
        self.assertIn('Иван Борисович Голубых', response.content.decode(),
                      msg='На странице отсутствует моя ФИО '
                          '(в футере должна быть)')
        self.assertIn('Все права защищены', response.content.decode(),
                      msg='На странице отсутствует автоское право')

    @transaction.atomic()
    def test_weather_json(self):
        """ Тест на успешную выдчу данных в формате Json стрианицы погоды.
        """
        response = self.client.get(reverse('weather_json'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не возвращает код 200 OK')
        self.assertEqual(response['Content-Type'], 'application/json',
                         msg='Страница погоды (для ajax) работает неверно: '
                             'не возвращает тип данных application/json')

        response = self.client.get(reverse('main'))
        Weather_For_Json.objects.all().delete()
        response = self.client.get(reverse('weather_json'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не возвращает код 200 OK при  наличии сессии')
        self.assertEqual(response['Content-Type'], 'application/json',
                         msg='Страница погоды (для ajax) работает неверно: '
                             'не возвращает тип данных application/json при '
                             'наличии сессии')

        _test_time = timezone.now()
        _test_time += datetime.timedelta(seconds=901)
        with mock.patch('django.utils.timezone.now') as perm_mock:
            perm_mock.return_value = _test_time
            response = self.client.get(reverse('weather_json'))
            self.assertEqual(
                response.status_code, 200,
                msg='Страница погоды (для ajax) работает неверно:'
                    ' не возвращает код 200 OK при  наличии сессии'
            )
            self.assertEqual(
                response['Content-Type'], 'application/json',
                msg='Страница погоды (для ajax) работает неверно: '
                    'не возвращает тип данных application/json при '
                    'наличии сессии'
            )

        _test_time = timezone.now()
        _test_time += datetime.timedelta(seconds=901*2)
        with mock.patch('django.utils.timezone.now') as perm_mock:
            perm_mock.return_value = _test_time
            with mock.patch('requests.get') as perm_mock3:
                perm_mock3.return_value = None
                response = self.client.get(reverse('weather_json'))
                self.assertEqual(
                    response.status_code, 200,
                    msg='Страница погоды (для ajax) работает неверно:'
                        ' не возвращает код 200 OK при  наличии сессии'
                )
                self.assertEqual(
                    response['Content-Type'],
                    'application/json',
                    msg='Страница погоды (для ajax) работает неверно: '
                        'не возвращает тип данных application/json при '
                        'наличии сессии'
                )

        response = self.client.get(reverse('weather_json'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не возвращает код 200 OK')
        self.assertEqual(response['Content-Type'], 'application/json',
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не тип данных application/json')

    def test_examples_work(self):
        """ Тест на доступность страницы Примеры работ
        """
        response = self.client.get(reverse('examples_work'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Примеры работ работает неверно:'
                             ' не возвращает код 200 OK')

    def test_examples_work_python_django(self):
        """ Тест на доступность страницы Примеры работ на Python/Django
        """
        response = self.client.get(reverse('examples_work_python_django'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Примеры работ на Python/Django'
                             ' работает неверно: не возвращает код 200 OK')

    def test_examples_work_js(self):
        """ Тест на доступность страницы Примеры работ на JavaScript
        """
        response = self.client.get(reverse('examples_work_js'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Примеры работ на JavaScript'
                             ' работает неверно: не возвращает код 200 OK')

    def test_examples_work_html_css(self):
        """ Тест на доступность страницы Примеры работ на Html5/Css3
        """
        response = self.client.get(reverse('examples_work_html_css'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Примеры работ на Html5/Css3'
                             ' работает неверно: не возвращает код 200 OK')

    def test_education(self):
        """ Тест на доступность страницы Учёбы
        """
        response = self.client.get(reverse('education'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Учёбы работает неверно:'
                             ' не возвращает код 200 OK')

    def test_works(self):
        """ Тест на доступность страницы Работы
        """
        response = self.client.get(reverse('works'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Работы работает неверно:'
                             ' не возвращает код 200 OK')

    def test_contact(self):
        """ Тест на доступность страницы Контакты
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница Контакты работает неверно:'
                             ' не возвращает код 200 OK')
