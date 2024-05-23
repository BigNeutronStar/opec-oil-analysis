import flet as ft
from flet_route import Params, Basket


def Page9(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/page9/:name9",
        controls=[
            ft.ElevatedButton("Вернуться выбору графиков", on_click=lambda _: page.go("/page1/:name1"), icon=ft.icons.ARROW_BACK)
        ]
    )