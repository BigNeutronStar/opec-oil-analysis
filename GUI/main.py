import flet as ft
from flet_route import Routing, path
from views.home import Home
from views.page1 import Page1
from views.page2 import Page2
from views.page3 import Page3
from views.page4 import Page4
from views.page5 import Page5
from views.page6 import Page6
from views.page7 import Page7
from views.page8 import Page8
from views.page9 import Page9
def main(page: ft.Page):

    app_routes = [

        path(url = "/", clear = True, view=Home),
        path(url = "/page1/:name1", clear = True, view=Page1),
        path(url = "/page2/:name2", clear = True, view=Page2),
        path(url = "/page3/:name3", clear = True, view=Page3),
        path(url="/page5/:name5", clear=True, view=Page5),
        path(url="/page4/:name4", clear=True, view=Page4),
        path(url="/page6/:name6", clear=True, view=Page6),
        path(url="/page7/:name7", clear=True, view=Page7),
        path(url="/page8/:name8", clear=True, view=Page8),
        path(url="/page9/:name9", clear=True, view=Page9)
    ]

    Routing(page=page,
            app_routes=app_routes,)

    page.go(page.route)

ft.app(target = main)