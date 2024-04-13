import flet as ft
from typing import Union
from flet_route import Params, Basket
def Home(page: ft.Page, params: Params, basket: Basket):
    
    content = ft.Column(
               
            [
                ft.Row(
                [
                    ft.Text("Navigation", size=30), 
                    ft.IconButton(icon=ft.icons.HOME, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.FilledButton("Graphics", icon=ft.icons.STACKED_LINE_CHART, on_click= lambda _: page.go("/page1/FletApp"),width=250,height=75)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.FilledButton("Use your data", icon=ft.icons.FILE_UPLOAD, on_click=lambda _: page.go("/page2/FletApp"),width=250,height=75)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.FilledButton("Information about project", icon=ft.icons.MENU_BOOK_ROUNDED, on_click=lambda _: page.go("/page3/FletApp"),width=250,height=75)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        )
    
    
    return content
