import flet as ft
from flet_route import Params, Basket


def Graphics(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        '/graphics',
        scroll=True,
        controls = [
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
        ]
    )
