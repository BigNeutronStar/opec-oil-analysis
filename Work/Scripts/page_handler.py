from math import pi
import time
import flet as ft
from flet_route import Routing, path

from Library.pages import Home
from Library.pages import Graphics
from Library.pages import Reports
from Library.pages import Info
from Library.pages import Loading
from Library.pages import ViewData
from Library.pages import setup_table_views

from Library import data

dates = countries = daily_production = main = ft.DataTable()

from Scripts import data_collector

def setup_page(page: ft.Page):
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    theme.page_transitions.linux = ft.PageTransitionTheme.NONE
    page.theme = theme
    page.theme_mode = 'dark'
    
    page.window_full_screen = True
    page.window_max_width = page.window_width
    page.window_full_screen = False

    page.window_maximized = True
    page.window_width = page.window_max_width

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_min_height = 800
    page.window_min_width = 700
    page.spacing = 0
    page.padding = 0

    app_routes = [
        path(url = "/", clear = True, view=Loading),
        path(url = "/home", clear = True, view=Home),
        path(url = "/graphics", clear=True, view=Graphics),
        path(url = "/info", clear=True, view=Info),
        path(url = "/view_data", clear=True, view=ViewData),
        path(url = "/reports", clear=True, view=Reports),
    ]

    Routing(page=page,
            app_routes=app_routes)

    page.update()

def create_table_views():
    global dates, countries, daily_production, main
    dates = data_collector.generate_datatable(data.dates)
    countries = data_collector.generate_datatable(data.countries)
    daily_production = data_collector.generate_datatable(data.daily_production)
    main = data_collector.generate_datatable(data.main)

def run_app(page: ft.Page):
    page.go(page.route)
    data_collector.read_data()
    create_table_views()
    setup_table_views(dates, countries, daily_production, main)
    page.go('/home')

    
     
    