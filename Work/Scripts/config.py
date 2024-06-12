"""Модуль для загрузки и хранения конфигурационных параметров из файла
config.ini и работы с ними."""
import configparser


class Config:
    """
    Класс для загрузки и хранения конфигурационных параметров.

    Автор: 
    Рахматуллин Айгиз
    """

    def __init__(self, config):
        """
        Инициализация класса Config.

        Вход:
        config (configparser.ConfigParser): Объект ConfigParser с загруженной конфигурацией.
        """
        self.report_dir = config['directories']['report_dir']
        self.personal_dir = config['directories']['personal_dir']

        self.databases = config['databases']
        self.personal_databases = config['personal_databases']
        self.graphics = config['graphics']
        self.loading_gif = config['loading_gif']['custom_loading']


def load():
    """
    Функция для загрузки конфигурации из файла.

    Вход:
    нет.

    Выход:
    config (Config): Экземпляр класса Config с загруженной конфигурацией.

    Автор: 
    Рахматуллин Айгиз
    """
    config = configparser.ConfigParser()
    config.read('Scripts/config.ini')

    return Config(config)
