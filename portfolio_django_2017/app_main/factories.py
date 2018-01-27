import factory
import random
import string
from . import models

__author__ = 'Иван Голубых'


class Weather_For_JsonFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Weather_For_Json


class MainHeader1TextFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)

    class Meta:
        model = models.MainHeader1Text


class MainHeader2TextFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    up = factory.SubFactory(MainHeader1TextFactory)

    class Meta:
        model = models.MainHeader2Text


class MainHeader3TextFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    up = factory.SubFactory(MainHeader2TextFactory)

    class Meta:
        model = models.MainHeader3Text


class MainHeader4TextFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    up = factory.SubFactory(MainHeader3TextFactory)

    class Meta:
        model = models.MainHeader4Text


class MainTextFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    up = factory.SubFactory(MainHeader4TextFactory)

    class Meta:
        model = models.MainText


class ExamplesPythonFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    name_project = ''.join(random.choice(string.printable) for _ in range(255))
    text = ''.join(random.choice(string.printable) for _ in range(300))

    class Meta:
        model = models.ExamplesPython


class ExamplesJsFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    name_project = ''.join(random.choice(string.printable) for _ in range(255))
    text = ''.join(random.choice(string.printable) for _ in range(300))

    class Meta:
        model = models.ExamplesJs


class ExamplesHtmlCssFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    name_project = ''.join(random.choice(string.printable) for _ in range(255))
    text = ''.join(random.choice(string.printable) for _ in range(300))

    class Meta:
        model = models.ExamplesHtmlCss


class EducationFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    text = ''.join(random.choice(string.printable) for _ in range(300))

    class Meta:
        model = models.Education


class WorksFactory(factory.DjangoModelFactory):
    ordinal = random.randint(0, 10000)
    text = ''.join(random.choice(string.printable) for _ in range(300))

    class Meta:
        model = models.Works
