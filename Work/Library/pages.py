import flet as ft
from flet_route import Params, Basket

def TitleBar(page: ft.page):
    def maximize_win(e):
        page.window_maximized = True
        page.update()

    def minimize_win(e):
        page.window_minimized = True
        page.update()
    
    return ft.ResponsiveRow(
        [   
            ft.WindowDragArea(
                content = ft.Container(
                    width = page.window_width,
                    expand=True,
                    margin=0,
                    content = ft.Row(
                        [
                                    ft.FilledButton(
                                        content = ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.MINIMIZE_OUTLINED, size=9)
                                            ]
                                        ),
                                        style=ft.ButtonStyle(
                                            color={
                                                ft.MaterialState.HOVERED: ft.colors.WHITE,
                                                ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                                            },
                                            bgcolor={
                                                ft.MaterialState.HOVERED: ft.colors.BLUE_200,
                                                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                                            },
                                            overlay_color=ft.colors.TRANSPARENT,
                                            animation_duration = 0,
                                            shape = ft.BeveledRectangleBorder(),
                                        ),
                                        on_click=minimize_win,
                                    ),
                                    ft.FilledButton(
                                        content = ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.CHECK_BOX_OUTLINE_BLANK, size=9)
                                            ]
                                        ),
                                        style=ft.ButtonStyle(
                                            color={
                                                ft.MaterialState.HOVERED: ft.colors.WHITE,
                                                ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                                            },
                                            bgcolor={
                                                ft.MaterialState.HOVERED: ft.colors.BLUE_200,
                                                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                                            },
                                            overlay_color=ft.colors.TRANSPARENT,
                                            shape = ft.BeveledRectangleBorder(),
                                            padding = 0,
                                        ),
                                        on_click=maximize_win,
                                    ),
                                    ft.FilledButton(
                                        content = ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.CLOSE, size=9)
                                            ]
                                        ),
                                        style=ft.ButtonStyle(
                                            color={
                                                ft.MaterialState.HOVERED: ft.colors.WHITE,
                                                ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                                            },
                                            bgcolor={
                                                ft.MaterialState.HOVERED: ft.colors.RED,
                                                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                                            },
                                            overlay_color=ft.colors.TRANSPARENT,
                                            animation_duration = 0,
                                            shape = ft.BeveledRectangleBorder(),
                                            padding = 0,
                                        ),
                                        on_click=lambda _: page.window_close(),
                                    ),
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ),
                height=20
            ),
            
        ]
    )

def Loading(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/",
        [   
            TitleBar(page),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.ProgressRing(),
                                ft.Text("Загрузка данных"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        ],
        padding = 0,
    )

   
def Home(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/home",
        [   
            TitleBar(page),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Навигация", size=30), 
                                ft.Icon(name=ft.icons.HOME, size=30),
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Графики", icon=ft.icons.STACKED_LINE_CHART, on_click= lambda _: page.go("/graphics"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Просмотр данных", icon=ft.icons.FILE_UPLOAD, on_click=lambda _: page.go("/view_data"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("О проекте", icon=ft.icons.MENU_BOOK_ROUNDED, on_click=lambda _: page.go("/info"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ],
        padding = 0,
    )

def Graphics(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/graphics',
        scroll=True,
        controls = [
            TitleBar(page),
            ft.ElevatedButton("Домой", on_click= lambda _: page.go("/home"),icon=ft.icons.ARROW_BACK),
            ft.Column(
                [
                        ft.Row(
                            [
                                ft.Text("Графики", size=30), 
                                ft.Icon(name=ft.icons.STACKED_LINE_CHART, size=30),
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Box&Whiskers", on_click= lambda _: page.go("/page4/FletApp"),width=250,height=55),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Категоризированная\nгистограмма", on_click= lambda _: page.go("/page5/FletApp"),width=250,height=55),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Кластеризованная\nдиаграмма", on_click= lambda _: page.go("/page6/FletApp"),width=250,height=55),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Рассеивание", on_click= lambda _: page.go("/page7/FletApp"),width=250,height=55),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Американские горки", on_click= lambda _: page.go("/page8/FletApp"),width=250,height=55),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                ]
            )
        ],
        padding = 0,
    )

def Info(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/info',
        controls = [   
            TitleBar(page),
            ft.ElevatedButton("Домой", on_click= lambda _: page.go("/home"),icon=ft.icons.ARROW_BACK),
            ft.Container(
                content = ft.Column(
                    [   
                        ft.Row(
                            [
                                ft.Text(
                                    spans = [
                                        ft.TextSpan(
                                            "В данном приложении вы можете создать собственые графики,\nиспользуя удобный интерфейс, "
                                            "а также просмотреть графики, уже созданные нами.\nАвторы приложения:\n Наумов Виталий\n Куров Егор\n"
                                            " Мирумян Артём\n Рахматуллин Айгиз",
                                        )
                                    ],
                                    color="#00008b", size=20, text_align="CENTER"
                                ),
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ],
        padding = 0,
    )

def ViewData(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/view_data',
        controls = [   
            TitleBar(page),
            ft.ElevatedButton("Домой", on_click= lambda _: page.go("/home"),icon=ft.icons.ARROW_BACK),
        ],
        padding = 0,
    )
