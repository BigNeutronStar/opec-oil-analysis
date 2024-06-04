import flet as ft
from flet_route import Routing, path

import os

from Scripts import config
from Library import data_collector, graphics_generator

from Scripts.views import Home, Loading, Graphics, DataTables, Info

def main(page: ft.Page):
    def route_change(e):
        if page.route == "/":
            page.views.clear()
            page.views.append(Loading(page))
        elif page.route == "/home":
            page.views.clear()
            page.views.append(Home(page))
        elif page.route == "/graphics":
            page.views.clear()
            page.views.append(Graphics(page, graphGenerator))
        elif page.route == '/datatables':
            page.views.clear()
            page.views.append(DataTables(page, data, personal_data, uploader))
        elif page.route == "/info":
            page.views.clear()
            page.views.append(Info(page))
        page.update()

    page.on_route_change = route_change

    page.go(page.route)

    cfg = config.Load()

    data = data_collector.Data()
    data.read_data(cfg.databases)

    personal_data = data_collector.Data()
    
    uploader=data_collector.Uploader(cfg.personal_dir)


    graphGenerator = graphics_generator.GraphGenerator(data, personal_data, cfg.graphics_dir)
    #reportGenerator = report_generator.ReportGenerator(data, personal_data, cfg.report_dir)

    page.go('/home')
    
if __name__ == "__main__":
    ft.app(target=main)


