import flet as ft
from flet_route import Params, Basket


def Page1(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page1/:name1",

        controls = [
            ft.ElevatedButton("Вернуться домой", on_click= lambda _: page.go("/"),icon=ft.icons.ARROW_BACK),
            ft.Column(
                [
            ft.Row(
                [
                    ft.Text("Графики", size=30), 
                    ft.IconButton(icon=ft.icons.STACKED_LINE_CHART, icon_size=30),

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
                    ft.ElevatedButton("Категоризированная гистограмма", on_click= lambda _: page.go("/page5/FletApp"),width=250,height=55),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Кластеризованная диаграмма", on_click= lambda _: page.go("/page6/FletApp"),width=250,height=55),
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
            ),
            ft.Column(
                [
            ft.Row(
                [
                    ft.Container(
                    ft.ElevatedButton("Построить по собственным данным",on_click= lambda _: page.go("/page9/FletApp"),width=300,height=55),
                    margin=100,
                    )
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ]
    )
