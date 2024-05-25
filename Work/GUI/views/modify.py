import flet as ft
from flet_route import Params, Basket

def Modify(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/modify',
        [   
            ft.ElevatedButton("Домой", on_click= lambda _: page.go("/home"),icon=ft.icons.ARROW_BACK),
        ]
    )


