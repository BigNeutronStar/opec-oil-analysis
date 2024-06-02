import flet as ft
from Scripts import page_handler
from Scripts import data_collector

def main(page: ft.Page):
    page_handler.setup_page(page)
    page_handler.run_app(page)
    
if __name__ == "__main__":
    ft.app(target = main)

