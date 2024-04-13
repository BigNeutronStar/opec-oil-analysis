import flet as ft
from flet_route import Params, Basket

def Page1(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page1/:name1",

        controls = [

            ft.Text("Графики"),
            ft.ElevatedButton("Назад", on_click= lambda _: page.go("/")),
        ]
    )

