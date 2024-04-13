import flet as ft
from flet_route import Params, Basket

def Page3(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page3/:name3",

        controls = [

            ft.Text(" This is page3 view"),
            ft.ElevatedButton(" Go back to home", on_click= lambda _: page.go("/"))
        ]
    )