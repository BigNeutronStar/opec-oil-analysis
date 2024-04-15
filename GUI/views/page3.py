import flet as ft
from flet_route import Params, Basket


def Page3(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/page3/:name3",

        controls=[
            ft.ElevatedButton(
                " Go back to home",
                on_click=lambda _: page.go("/"),
                icon = ft.icons.ARROW_BACK
            ),
            ft.Text(
                "В данном приложении вы можете создать собственыые графики, используя удобный интерфейс, "
                "а также просмотреть графики, уже созданные нами.\nАвторы приложения:\n Наумов Виталий\n Куров Егор\n"
                " Мирумян Артём\n Рахматуллин Айгиз\n Все студенты группы БИВ234",
                color="#00008b", size=40,weight=ft.FontWeight.BOLD),

        ]
    )


