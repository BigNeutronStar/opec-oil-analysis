import flet as ft
import sys

from flet_route import Routing, path
from GUI.views.home import Home
from GUI.views.graphics import Graphics
from GUI.views.info import Info
from GUI.views.loading import Loading
from GUI.views.modify import Modify

from Scripts import data_collector
from Scripts import report_generator
from Scripts import graphics_generator

def main(page: ft.Page):
    page.title = "Анализ данных"
    app_routes = [
        path(url = "/", clear=True, view=Loading),
        path(url = "/home", clear=True, view=Home),
        path(url = "/graphics", clear=True, view=Graphics),
        path(url = "/info", clear=True, view=Info),
        path(url="/modify", clear=True, view=Modify)
    ]

    Routing(page=page, app_routes=app_routes)
    #page.go(page.route)
    #data_collector.read_data()
    page.go("/home")

ft.app(target = main)


#for param in sys.argv[1:]:
#        if param == '-g':
#                data_collector.generate_main()

