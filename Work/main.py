"""
Модуль `main` является входной точкой приложения Flet. Он содержит главную 
функцию для инициализации и управления приложением.

Функции:
- main: Главная функция для инициализации и управления приложением Flet.

Модули:
- flet: Модуль, предоставляющий основные инструменты для создания веб-приложений.
- Scripts.config: Модуль, содержащий конфигурационные параметры приложения.
- Library.data_collector: Модуль для сбора данных из источников.
- Library.graphics_generator: Модуль для генерации графиков на основе данных.
- Library.report_generator: Модуль для создания отчетов на основе данных.
- Scripts.views: Модули, содержащие классы для отображения различных страниц приложения.

Автор: Наумов Виталий
"""

import time
import flet as ft
from Scripts import config
from Scripts.views import Home, Loading, Graphics, DataTables, Reports, Info
from Library import data_collector, graphics_generator, report_generator


def main(page: ft.Page):
    """
    Главная функция для инициализации и управления приложением Flet.

    Вход:
    page (ft.Page): Экземпляр страницы Flet.

    Автор: Наумов Виталий
    """

    def route_change(e):
        """
        Обработчик изменения маршрута.

        Вход:
        e (Event): Событие изменения маршрута.

        Автор: Наумов Виталий
        """
        if page.route == "/":
            page.views.clear()
            page.views.append(Loading(page, cfg.loading_gif))
        elif page.route == "/home":
            page.views.clear()
            page.views.append(Home(page))
        elif page.route == "/graphics":
            page.views.clear()
            page.views.append(Graphics(page, g_generator))
        elif page.route == '/datatables':
            page.views.clear()
            page.views.append(DataTables(page, data, personal_data, uploader))
        elif page.route == '/reports':
            page.views.clear()
            page.views.append(Reports(page, r_generator))
        elif page.route == "/info":
            page.views.clear()
            page.views.append(Info(page))
        page.update()

    cfg = config.load()

    page.on_route_change = route_change

    page.go(page.route)

    data = data_collector.Data()
    data.read_data(cfg.databases)
    data.set_priority()

    personal_data = data_collector.Data()
    personal_data.read_data(cfg.personal_databases)

    uploader = data_collector.Uploader(cfg.personal_dir)

    g_generator = graphics_generator.GraphGenerator(
        data, personal_data, cfg.graphics)
    r_generator = report_generator.ReportGenerator(
        data, personal_data, cfg.report_dir)

    time.sleep(2)

    page.go('/home')


if __name__ == "__main__":
    ft.app(target=main)
