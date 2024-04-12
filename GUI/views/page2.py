import flet as ft
from flet_route import Params, Basket

def Page2(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page2/:name2",

        controls = [

            ft.Text(" This is page 2 view"),
            ft.ElevatedButton(" Go back to home", on_click= lambda _: page.go("/"))
        ]
    )

