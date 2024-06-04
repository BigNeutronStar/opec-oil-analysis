import flet as ft
from flet_route import Params, Basket

import os

class TitleBar(ft.ResponsiveRow):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.initialize_controls()

    def initialize_controls(self):
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
                            self.get_bar_button(self.minimize_window, ft.icons.MINIMIZE_OUTLINED),
                            self.get_bar_button(self.maximize_window, ft.icons.CHECK_BOX_OUTLINE_BLANK),
                            self.get_bar_button(self.window_close, ft.icons.CLOSE, ft.colors.RED),
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ),
                height=20
            )
        ]

    def maximize_window(self, e):
        self.page.window_maximized = True
        self.page.update()

    def minimize_window(self, e):
        self.page.window_minimized = True
        self.page.update()
    
    def window_close(self, e):
        self.page.window_close()

    def get_bar_button(self, on_click_func, icon, hovered_color=ft.colors.BLUE_200):
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
    def __init__(self, page, padding=0, scroll=False):
        super().__init__(scroll = scroll, padding=padding)
        self.page = page

        self.setup_theme()
        self.setup_sizes()
        self.page.update()

        self.page.window_maximized = True
        self.page.update()
    
    def setup_theme(self):
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
        self.page.window_min_height = 800
        self.page.window_min_width = 700
        self.page.spacing = 0
        self.page.padding = 0