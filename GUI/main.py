import flet as ft
from flet_route import Routing, path
from views.home import Home
from views.page1 import Page1
from views.page2 import Page2
from views.page3 import Page3

def main(page: ft.Page):

    app_routes = [

        path(url = "/", clear = True, view=Home),
        path(url = "/page1/:name1", clear = True, view=Page1),
        path(url = "/page2/:name2", clear = True, view=Page2),
        path(url = "/page3/:name3", clear = True, view=Page3)
        
    ]

    Routing(page=page,
            app_routes=app_routes,)

    page.go(page.route)

ft.app(target = main)