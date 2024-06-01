import subprocess
from math import pi
import shutil
import os
import flet as ft
from flet_route import Params, Basket
from flet.matplotlib_chart import MatplotlibChart
import matplotlib
from Scripts import graphics_generator
from Library import data

def TitleBar(page: ft.Page):
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
    def open_configure_window(plot_func, atr='', countries_disabled=False):
        start = min(data.get_years())
        end = max(data.get_years())

        def change_period(e):
            nonlocal start, end
            start = e.control.start_value
            start = round(float(start))
            end = e.control.end_value
            end = round(float(end))
        
        def build_new(e):
            nonlocal start, end
            countries = [el.label for el in countries_checkboxes if el.value]
            if not countries_disabled:
                if atr == '':
                    fig = plot_func(start, end, countries)
                else:
                    fig = plot_func(atr, start, end, countries)
            else:
                fig = plot_func(atr, start, end)
            put_graph(fig)

        countries_checkboxes = []
        for c in data.get_countries():
            countries_checkboxes.append(ft.Checkbox(label=c, disabled=countries_disabled, value=True))
        page.views[0].controls[2].content.controls[0].controls = [
            ft.Container(
                content = ft.Column(
                    [   
                        ft.Column(
                            [
                                ft.Text("Период",  weight=ft.FontWeight.BOLD,),
                                ft.RangeSlider(
                                    min=min(data.get_years()),
                                    max=max(data.get_years()),
                                    start_value=2006,
                                    divisions=17,
                                    end_value=2022,
                                    inactive_color=ft.colors.BLUE_100,
                                    active_color=ft.colors.BLUE_500,
                                    overlay_color=ft.colors.BLUE_200,
                                    label="{value}",
                                    on_change=change_period,
                                ),
                            ]
                        ),
                        ft.Column(
                            [ft.Text("Страны",  weight=ft.FontWeight.BOLD)] + countries_checkboxes
                        ),
                        ft.ElevatedButton(
                            "Построить",
                            on_click=build_new,
                            disabled=True
                        )
                    ],
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.START
                ),
                padding = 10,
            )
            
        ]

        page.views[0].controls[2].content.controls[2].controls = [
            ft.ElevatedButton("Сохранить график",
                                disabled=True
            )
        ]
        page.update()
        build_new(0)
        
    
    def put_graph(fig):
        file_picker = ft.FilePicker(on_result=lambda e: graphics_generator.save_graph(fig, e.path))
        page.overlay.append(file_picker)

        page.views[0].controls[2].content.controls[1].controls = [ft.ProgressRing()]
        page.views[0].controls[2].content.controls[2].controls[0].disabled=True
        page.update()
        page.views[0].controls[2].content.controls[1].controls = [MatplotlibChart(fig)]
        page.views[0].controls[2].content.controls[2].controls[0].on_click = lambda _: file_picker.save_file(allowed_extensions=['png'])
        page.views[0].controls[2].content.controls[2].controls[0].disabled=False
        page.views[0].controls[2].content.controls[0].controls[0].content.controls[2].disabled=False
        page.update()
        
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
                                        on_click = lambda _: open_configure_window(graphics_generator.plot_graph, 'Курс', countries_disabled=True)
                                    ),
                        
                                    ft.MenuItemButton(
                                        content=ft.Text("Цена на нефть"),
                                        on_click = lambda _: open_configure_window(graphics_generator.plot_graph, 'Цена', countries_disabled=True)
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
                                        on_click = lambda _: open_configure_window(graphics_generator.plot_boxwhiskers, 'Курс', countries_disabled=True)
                                    ),
                        
                                    ft.MenuItemButton(
                                        content=ft.Text("Цена на нефть"),
                                        on_click = lambda _: open_configure_window(graphics_generator.plot_boxwhiskers, 'Цена', countries_disabled=True)
                                    ),
                            
                                    ft.MenuItemButton(
                                        content=ft.Text("Добыча нефти"),
                                        on_click = lambda _: open_configure_window(graphics_generator.plot_boxwhiskers, 'Добыча')
                                    ),
                                ]
                            ),
                            
                            ft.MenuItemButton(
                                content=ft.Text("Гистограмма"),
                                on_click=lambda _: open_configure_window(graphics_generator.hist)
                            ),
                            
                            ft.MenuItemButton(
                                content=ft.Text("Диаграмма"),
                                on_click=lambda _: open_configure_window(graphics_generator.diag)
                            ),
                            
                            ft.SubmenuButton(
                                content=ft.Text("Рассеивание"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("По цене"),
                                        on_click=lambda _: open_configure_window(graphics_generator.plot_scatter, 'Цена')
                                    ),
                        
                                    ft.MenuItemButton(
                                        content=ft.Text("По курсу"),
                                        on_click=lambda _: open_configure_window(graphics_generator.plot_scatter, 'Курс')
                                    ),
                                ]
                            )
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(
                content=ft.Row(
                    [   
                        ft.Column(
                            [

                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width = page.window_width / 4,
                        ),

                        ft.Column(
                            [
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width = page.window_width / 2,
                        ),

                        ft.Column(
                            [

                            ],
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width = page.window_width / 4,
                        ),
                    ]
                ),
                alignment=ft.alignment.center,
                width = page.window_width,
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
                                    color="white", size=20, text_align="CENTER"
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
        padding = 10,
    )

