import flet as ft
from typing import Union
from flet_route import Params, Basket

def Home(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/home",
        [   
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
                                ft.ElevatedButton("Модификация данных", icon=ft.icons.FILE_UPLOAD, on_click=lambda _: page.go("/modify"),width=250,height=75)
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
        ]
    )
