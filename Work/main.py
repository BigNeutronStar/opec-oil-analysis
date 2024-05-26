import flet as ft
from flet_route import Routing

from Scripts import page_handler
#from Scripts import report_generator
#from Scripts import graphics_generator

def main(page: ft.Page):
    page_handler.setup_page(page)
    page_handler.start(page)

if __name__ == "__main__":
    ft.app(target = main)

