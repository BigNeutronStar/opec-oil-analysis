from math import pi
import time
import flet as ft
from flet_route import Routing, path

from Library.pages import Home
from Library.pages import Graphics
from Library.pages import Info
from Library.pages import Loading
from Library.pages import ViewData

from Scripts import data_collector

def start(page: ft.Page):
    page.go(page.route)
    data_collector.read_data()
    page.go('/home')
    
def setup_page(page: ft.Page):
    page.theme_mode='dark'
    page.window_maximized = True
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_min_height = 800
    page.window_min_width = 700
    page.spacing = 0
    page.padding = 0
    Routing(page=page,
            app_routes=get_routes())

def get_routes():
    app_routes = [
        path(url = "/", clear = True, view=Loading),
        path(url = "/home", clear = True, view=Home),
        path(url = "/graphics", clear=True, view=Graphics),
        path(url = "/info", clear=True, view=Info),
        path(url = "/view_data", clear=True, view=ViewData),
    ]
    return app_routes