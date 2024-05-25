import flet as ft
from flet_route import Params, Basket

def Info(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/info',
        [   
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
                                    color="#00008b", size=20, text_align="CENTER"
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
        ]
    )


