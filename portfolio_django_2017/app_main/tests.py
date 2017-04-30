from django.test import TestCase
from django.core.urlresolvers import reverse


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
        response = self.client.get(reverse('main'))
        self.assertIn('>Главная</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>Примеры работ</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>Учёбы</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>Работы</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>Контакты</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')

    def test_main_page_futer(self):
        """ Тест на наличие всех обязательных текстов в футере:
        8-921-355-04-60, ivan9@allworld.xyz, kreoya, Иван Борисович Голубых,
        Все права защищены.
        """
        response = self.client.get(reverse('main'))
        self.assertIn('8-921-355-04-60', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>ivan9@allworld.xyz</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('>kreoya</a>', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('Иван Борисович Голубых', response.content.decode(),
                      msg='На странице отсутствует меню Главная')
        self.assertIn('Все права защищены', response.content.decode(),
                      msg='На странице отсутствует меню Главная')

    def test_weather_json(self):
        """ Тест на успешную выдчу данных в формате Json стрианицы погоды.
        """
        response = self.client.get(reverse('weather_json'))
        self.assertEqual(response.status_code, 200,
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не возвращает код 200 OK')
        self.assertEqual(response['Content-Type'], 'application/json',
                         msg='Страница погоды (для ajax) работает неверно:'
                             ' не тип данных application/json')
