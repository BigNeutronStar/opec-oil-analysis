"""
Модуль Components

Этот модуль предоставляет компоненты для создания пользовательского интерфейса
в приложении на базе Flet.

Классы:
    TitleBar: Кастомная строка заголовка для окна приложения.
    Page: Кастомное представление страницы для приложения.

Автор:
    Куров Егор
    Мирумян Артем
"""

import os
import flet as ft


class TitleBar(ft.ResponsiveRow):
    """
    Кастомная строка заголовка для окна приложения.

    Этот класс создает строку заголовка с кнопками свернуть, развернуть и закрыть 
    для систем, отличных от posix.
    """

    def __init__(self, page: ft.Page):
        """
        Инициализация TitleBar.

        Вход:
        page (ft.Page): Объект страницы, представляющий окно приложения.

        Автор: 
        Куров Егор
        """
        super().__init__()
        self.page = page
        self.initialize_controls()

    def initialize_controls(self):
        """
        Инициализация элементов управления для строки заголовка.

        Добавляет кнопки свернуть, развернуть и закрыть в строку заголовка для Windows

        Автор: 
        Куров Егор
        """
        if os.name == 'posix':
            return

        self.controls = [
            ft.WindowDragArea(
                content=ft.Container(
                    width=self.page.window_width,
                    expand=True,
                    margin=0,
                    content=ft.Row(
                        [
                            self.get_bar_button(lambda _:
                                                self.minimize_window(), ft.icons.MINIMIZE_OUTLINED),
                            self.get_bar_button(lambda _:
                                                self.maximize_window(), ft.icons.CHECK_BOX_OUTLINE_BLANK),
                            self.get_bar_button(lambda _:
                                                self.window_close(), ft.icons.CLOSE, ft.colors.RED),
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ),
                height=20
            )
        ]

    def maximize_window(self):
        """
        Развернуть окно приложения.


        Автор: 
        Куров Егор
        """
        self.page.window_maximized = True
        self.page.update()

    def minimize_window(self):
        """
        Свернуть окно приложения.


        Автор: 
        Куров Егор
        """
        self.page.window_minimized = True
        self.page.update()

    def window_close(self):
        """
        Закрыть окно приложения.

        Автор: 
        Куров Егор
        """
        self.page.window_close()

    def get_bar_button(self, on_click_func, icon, hovered_color=ft.colors.BLUE_200):
        """
        Создать кнопку для строки заголовка.

        Вход:
        on_click_func (function): Функция, вызываемая при нажатии на кнопку.
        icon (ft.icons): Иконка, отображаемая на кнопке.
        hovered_color (ft.colors): Цвет кнопки при наведении. По умолчанию BLUE_200.

        Выход:
        ft.FilledButton: Созданная кнопка.

        Автор: 
        Куров Егор
        """
        return ft.FilledButton(
            content=ft.Row(
                [
                    ft.Icon(name=icon, size=9)
                ]
            ),
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                },
                bgcolor={
                    ft.MaterialState.HOVERED: hovered_color,
                    ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                },
                overlay_color=ft.colors.TRANSPARENT,
                animation_duration=0,
                shape=ft.BeveledRectangleBorder(),
            ),
            on_click=on_click_func
        )


class Page(ft.View):
    """
    Кастомное представление страницы для приложения.

    Этот класс настраивает тему и размеры окна приложения.
    """

    def __init__(self, page, padding=0, scroll=False):
        """
        Инициализация Page.

        Вход:
        page (ft.Page): Объект страницы, представляющий окно приложения.
        padding (int): Отступ для страницы. По умолчанию 0.
        scroll (bool): Включение или отключение прокрутки. По умолчанию False.

        Автор: 
        Мирумян Артем
        """
        super().__init__(scroll=scroll, padding=padding)
        self.page = page

        self.setup_theme()
        self.setup_sizes()
        self.page.update()

        self.page.window_maximized = True
        self.page.update()

    def setup_theme(self):
        """
        Настройка темы для окна приложения.

        Конфигурирует тему и переходы для различных операционных систем.

        Автор: 
        Мирумян Артем
        """
        theme = ft.Theme()
        theme.page_transitions.windows = ft.PageTransitionTheme.NONE
        theme.page_transitions.macos = ft.PageTransitionTheme.NONE
        theme.page_transitions.linux = ft.PageTransitionTheme.NONE

        self.page.theme = theme
        self.page.theme_mode = 'dark'

        if os.name == 'nt':
            self.page.window_title_bar_hidden = True
            self.page.window_title_bar_buttons_hidden = True

    def setup_sizes(self):
        """
        Настройка размеров окна приложения.

        Устанавливает минимальные размеры окна и отступы.

        Автор: 
        Мирумян Артем
        """
        self.page.window_min_height = 800
        self.page.window_min_width = 700
        self.page.spacing = 0
        self.page.padding = 0
