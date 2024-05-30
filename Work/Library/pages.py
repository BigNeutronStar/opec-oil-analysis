import subprocess
from math import pi
import shutil
import os
import flet as ft
from flet_route import Params, Basket
from flet.matplotlib_chart import MatplotlibChart
import matplotlib
from Scripts import graphics_generator


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
                    )  
        ], 
    )

###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ######
###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ######

def Reports(page: ft.Page, params: Params, basket: Basket):
    
    def run_report_generator():
        subprocess.run(["python3", "/Users/artem/Desktop/University/python-project-1/Work/Scripts/report_generator.py"])

        reports_dir = "/Users/artem/Desktop/University/python-project-1/Work/Output"
        reports = [f for f in os.listdir(reports_dir) if f.endswith(".txt")]
        return reports

    def open_reports_dialog(page: ft.Page, reports):
        report_contents = []
        for report in reports:
            with open(os.path.join("/Users/artem/Desktop/University/python-project-1/Work/Output", report), "r") as file:
                content = file.read()
                report_contents.append(ft.Text(content))

        page.dialog = ft.Dialog(
            content=ft.Container(
                content=ft.Column(
                    report_contents,
                    scroll=True,
                ),
                width=600,
                height=400,
                padding=20
            ),
            open=True
        )
        page.update()

    def on_create_reports_click(e):
        reports = run_report_generator()
        open_reports_dialog(e.page, reports)

    def download_report(page: ft.Page, report):
        report_path = os.path.join("/Users/artem/Desktop/University/python-project-1/Work/Output", report)
        with open(report_path, "rb") as file:
            file_contents = file.read()
            page.launch_file(file.name, file_contents)

    def on_download_reports_click(e):
        reports = [f for f in os.listdir("/Users/artem/Desktop/University/python-project-1/Work/Output") if f.endswith(".txt")]
        for report in reports:
            download_report(e.page, report)

    return ft.View(
        "/reports",
        [
            TitleBar(page),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Создать отчеты",
                                    on_click=on_create_reports_click,
                                    width=250,
                                    height=75
                                ),
                                ft.ElevatedButton(
                                    "Скачать отчеты",
                                    on_click=on_download_reports_click,
                                    width=250,
                                    height=75
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ],
        padding=0,
    )

###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ######
###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ###### REPORTS ######




###### LOADING ###### LOADING ###### LOADING ###### LOADING ###### LOADING ###### LOADING ######
###### LOADING ###### LOADING ###### LOADING ###### LOADING ###### LOADING ###### LOADING ######

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
                        ft.Row(
                            [
                                ft.ElevatedButton("Просмотр отчетов", icon=ft.icons.MENU_BOOK_ROUNDED, on_click=lambda _: page.go("/reports"),width=250,height=75)
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
    def put_plot(fig):
        page.views[0].controls[2] = ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.ProgressRing()
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
            width = page.window_width,
            height = page.window_height - 200
        ) 
        page.update()
        page.views[0].controls[2] = ft.Container(
            content=ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                MatplotlibChart(fig)
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
                width = page.window_width / 2,
            ),
            alignment=ft.alignment.center,
            width = page.window_width,
            height = page.window_height-200,
        ) 
        page.update()
        
    
    scatter_buttons = []
        
    
    return ft.View(
        '/graphics',
        scroll=True,
        controls = [
            TitleBar(page),
            ft.Row(
                [
                    ft.MenuBar(
                        style = ft.MenuStyle(
                            bgcolor=ft.colors.TRANSPARENT,
                            shadow_color=ft.colors.TRANSPARENT,
                        ),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Назад"),
                                on_click=lambda _: page.go('/home'),
                                style=ft.ButtonStyle(
                                    overlay_color=ft.colors.TRANSPARENT,
                                    animation_duration = 0,
                                ),
                            ),
                            
                            ft.SubmenuButton(
                                content=ft.Text("Графики изменения"),
                                style=ft.ButtonStyle(
                                    overlay_color=ft.colors.TRANSPARENT,
                                    animation_duration = 0,
                                    shape = ft.RoundedRectangleBorder(),
                                ),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("Курс рубля"),
                                        on_click = lambda _: put_plot(graphics_generator.plot_course())
                                    ),
                        
                                    ft.MenuItemButton(
                                        content=ft.Text("Цена на нефть"),
                                        on_click = lambda _: put_plot(graphics_generator.plot_price())
                                    ),
                                ]
                            ),
                            
                            ft.SubmenuButton(
                                content=ft.Text("Box & Whiskers"),
                                style=ft.ButtonStyle(
                                    overlay_color=ft.colors.TRANSPARENT,
                                    animation_duration = 0,
                                    shape = ft.RoundedRectangleBorder(),
                                ),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("Курс рубля"),
                                        on_click = lambda _: put_plot(graphics_generator.plot_boxwhiskers("Курс"))
                                    ),
                        
                                    ft.MenuItemButton(
                                        content=ft.Text("Цена на нефть"),
                                        on_click = lambda _: put_plot(graphics_generator.plot_boxwhiskers("Цена"))
                                    ),
                            
                                    ft.MenuItemButton(
                                        content=ft.Text("Добыча нефти"),
                                        on_click = lambda _: put_plot(graphics_generator.plot_boxwhiskers("Добыча"))
                                    ),
                        
                                ]
                            ),
                            
                            ft.MenuItemButton(
                                content=ft.Text("Гистограмма"),
                                on_click=lambda _: put_plot(graphics_generator.hist())
                            ),
                            
                            ft.MenuItemButton(
                                content=ft.Text("Диаграмма"),
                                on_click=lambda _: put_plot(graphics_generator.diag())
                            ),
                            
                            ft.SubmenuButton(
                                content=ft.Text("Рассеивание"),
                            )
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(
                
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

