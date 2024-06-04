import flet as ft

from flet.matplotlib_chart import MatplotlibChart

from Library.components import Page, TitleBar

class Home(Page):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page

        self.page.window_max_width = self.page.window_width

        self.controls = [
            TitleBar(page),
            self.initialize_body(page)
        ]
    
    def initialize_body(self, page):
        return ft.Container(
                content = ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Навигация", size=30), 
                                ft.Icon(name=ft.icons.HOME, size=30),
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Графики", icon=ft.icons.STACKED_LINE_CHART, on_click= lambda _: page.go("/graphics"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Просмотр данных", icon=ft.icons.FILE_UPLOAD, on_click=lambda _: page.go("/datatables"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Просмотр отчетов", icon=ft.icons.MENU_BOOK_ROUNDED, on_click=lambda _: page.go("/reports"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("О проекте", icon=ft.icons.MENU_BOOK_ROUNDED, on_click=lambda _: page.go("/info"),width=250,height=75)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True
            )

class Loading(Page):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page
        self.controls = [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.ProgressRing(),
                                ft.Text("Загрузка данных"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        ]

class Graphics(Page):
    def __init__(self, page: ft.Page, generator):
        super().__init__(page, scroll=True)
        self.page = page
        self.graphGenerator = generator

        self.dashboard_slider = ft.Container()
        self.dashboard_boxes = ft.Container()
        self.dashboard_button = ft.Container()
        self.graph = ft.Container()
        self.save_button = ft.Container()

        self.is_personal_data = not self.graphGenerator.personal_data.is_empty

        self.data_switch = ft.Switch(label="Использовать пользовательские данные", on_change=self.switch_data, disabled = not self.is_personal_data)

        self.controls = [
            TitleBar(page),
            self.get_navbar(),
            ft.Container()
        ]
    
    def switch_data(self, e):
        self.graphGenerator.switch_data()
        self.is_personal_data ^= True
        print(self.is_personal_data)
        self.page.update()
    
    def update_body(self):
        self.controls[-1] = ft.Container(
            content=ft.Row(
                [   
                    ft.Column(
                        [
                            ft.Container(
                                content = ft.Column(
                                    [   
                                        self.data_switch,
                                        self.dashboard_slider,
                                        self.dashboard_boxes,
                                        self.dashboard_button
                                    ],
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                ),
                                padding = 10,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width = self.page.window_max_width / 4,
                    ),

                    ft.Column(
                        [
                            self.graph
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width = self.page.window_max_width / 2,
                    ),

                    ft.Column(
                        [   
                            self.save_button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        width = self.page.window_max_width / 4,
                    ),
                ]
            ),
            alignment=ft.alignment.center,
            width = self.page.window_max_width,
        )
        self.page.update()
        
    def get_navbar(self):
        return ft.Row(
            [
                ft.MenuBar(
                    style = ft.MenuStyle(
                        bgcolor=ft.colors.TRANSPARENT,
                        shadow_color=ft.colors.TRANSPARENT,
                    ),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Назад"),
                            on_click=lambda _: self.page.go('/home'),
                        ),
                        
                        ft.SubmenuButton(
                            content=ft.Text("Графики изменения"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("Курс рубля"),
                                    on_click = lambda _: self.open_configure_window(self.graphGenerator.plot_graph, 'Курс', countries_disabled=True)
                                ),
                    
                                ft.MenuItemButton(
                                    content=ft.Text("Цена на нефть"),
                                    on_click = lambda _: self.open_configure_window(self.graphGenerator.plot_graph, 'Цена', countries_disabled=True)
                                ),
                            ]
                        ),
                        
                        ft.SubmenuButton(
                            content=ft.Text("Box & Whiskers"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("Курс рубля"),
                                    on_click = lambda _: self.open_configure_window(self.graphGenerator.plot_boxwhiskers, 'Курс', countries_disabled=True)
                                ),
                    
                                ft.MenuItemButton(
                                    content=ft.Text("Цена на нефть"),
                                    on_click = lambda _: self.open_configure_window(self.graphGenerator.plot_boxwhiskers, 'Цена', countries_disabled=True)
                                ),
                        
                                ft.MenuItemButton(
                                    content=ft.Text("Добыча нефти"),
                                    on_click = lambda _: self.open_configure_window(self.graphGenerator.plot_boxwhiskers, 'Добыча')
                                ),
                            ]
                        ),
                        
                        ft.MenuItemButton(
                            content=ft.Text("Гистограмма"),
                            on_click=lambda _: self.open_configure_window(self.graphGenerator.hist)
                        ),
                        
                        ft.MenuItemButton(
                            content=ft.Text("Диаграмма"),
                            on_click=lambda _: self.open_configure_window(self.graphGenerator.diag)
                        ),
                        
                        ft.SubmenuButton(
                            content=ft.Text("Рассеивание"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("По цене"),
                                    on_click=lambda _: self.open_configure_window(self.graphGenerator.plot_scatter, 'Цена')
                                ),
                    
                                ft.MenuItemButton(
                                    content=ft.Text("По курсу"),
                                    on_click=lambda _: self.open_configure_window(self.graphGenerator.plot_scatter, 'Курс')
                                ),
                            ]
                        )
                    ],
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    def open_configure_window(self, plot_func, atr='', countries_disabled=False):
        years = self.graphGenerator.current_data.years
        min_year, max_year = min(years), max(years)
        countries = self.graphGenerator.current_data.countries_list

        start, end = min_year, max_year

        def change_period(e):
            nonlocal start, end
            start = e.control.start_value
            start = round(float(start))
            end = e.control.end_value
            end = round(float(end))
        
        def build_new(e):
            self.graphGenerator.clear()
            countries = [el.label for el in countries_checkboxes if el.value]
            if not countries_disabled:
                if atr == '':
                    fig = plot_func(start, end, countries)
                else:
                    fig = plot_func(atr, start, end, countries)
            else:
                fig = plot_func(atr, start, end)
            self.put_graph(fig)

        countries_checkboxes = []
        for c in countries:
            countries_checkboxes.append(ft.Checkbox(label=c, disabled=countries_disabled, value=True))

        self.dashboard_slider =  ft.Column(
            [
                ft.Text("Период",  weight=ft.FontWeight.BOLD,),
                ft.RangeSlider(
                    min=min_year,
                    max=max_year,
                    start_value=2006,
                    divisions=17,
                    end_value=2022,
                    inactive_color=ft.colors.BLUE_100,
                    active_color=ft.colors.BLUE_500,
                    overlay_color=ft.colors.BLUE_200,
                    label="{value}",
                    on_change=change_period,
                ),
            ]
        )

        self.dashboard_boxes =  ft.Column(
            [ft.Text("Страны",  weight=ft.FontWeight.BOLD)] + countries_checkboxes
        )

        self.dashboard_button = ft.ElevatedButton(
            "Построить",
            on_click=build_new,
            disabled=True
        )
        
        self.save_button = ft.ElevatedButton("Сохранить график", disabled=True)
        build_new(None)
    
    def put_graph(self, fig):
        file_picker = ft.FilePicker(on_result=lambda e: self.graphGenerator.save_graph(fig, e.path))
        self.page.overlay.append(file_picker)

        self.graph = ft.ProgressRing()
        self.update_body()

        self.graph = MatplotlibChart(fig)
        self.save_button.on_click = lambda _: file_picker.save_file(allowed_extensions=['png'])
        self.save_button.disabled=False
        self.dashboard_button.disabled=False
        self.update_body()

class DataTables(Page):
    def __init__(self, page: ft.Page, data, personal_data, uploader):
        super().__init__(page)
        self.page = page
        self.data = data
        self.uploader = uploader
        self.personal_data = personal_data

        self.file_saver = ft.FilePicker(on_result=self.on_save_result)
        self.file_uploader = ft.FilePicker(on_result=self.on_upload_result)
        self.page.overlay.append(self.file_saver)
        self.page.overlay.append(self.file_uploader)
        self.file_name = None

        self.controls = [
            TitleBar(page),
            self.get_navbar(),
            ft.Row(
                [
                    self.get_table('ДАТА', 420, 500, self.data.generate_datatable(self.data.dates), self.get_save_button('dates')),
                    self.get_table('СТРАНЫ', 250, 500, self.data.generate_datatable(self.data.countries), self.get_save_button('countries')),
                    self.get_table('ДОБЫЧА', 350, 500, self.data.generate_datatable(self.data.daily_production), self.get_save_button('daily_production'))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                visible = True,
            ),
            ft.Row(
                [
                   
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                visible = False,
            ),
            ft.Row(
                [
                    ft.ElevatedButton('Очистить данные', on_click=self.clear_data)
                ],
                alignment=ft.MainAxisAlignment.END,
                visible = False,
            )
        ]

        self.update_personal_table()

    def update_personal_table(self):
        self.controls[-2].controls =  [
            self.get_table('ДАТА', 420, 500, self.personal_data.generate_datatable(self.personal_data.dates), self.get_upload_button('dates')),
            self.get_table('СТРАНЫ', 250, 500, self.personal_data.generate_datatable(self.personal_data.countries), self.get_upload_button('countries')),
            self.get_table('ДОБЫЧА', 350, 500, self.personal_data.generate_datatable(self.personal_data.daily_production), self.get_upload_button('daily_production'))
        ]
        self.page.update()
    
    def get_save_button(self, name):
        return ft.ElevatedButton('Экспортировать данные', data = name, on_click=self.save_data)
    
    def get_upload_button(self, name):
        return ft.ElevatedButton('Загрузить данные', data = name, on_click=self.upload_data)
    
    def get_table(self, name, width, height, table, button):
        return ft.Column(
            [
                ft.Text(name, weight = ft.FontWeight.BOLD),
                ft.Container(
                    width=width,
                    height=height,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                width=width,
                                content=ft.Column(
                                    controls=[
                                        table
                                    ]
                                ),
                            )
                        ],
                        scroll="auto",  
                    ),
                    border=ft.border.all(1, "blue"),
                ),
                button
            ]
        )
    
    def get_navbar(self):
        return ft.Row(
            [
                ft.MenuBar(
                    style = ft.MenuStyle(
                        bgcolor=ft.colors.TRANSPARENT,
                        shadow_color=ft.colors.TRANSPARENT,
                    ),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Назад"),
                            on_click=lambda _: self.page.go('/home'),
                        ),
                        
                        ft.MenuItemButton(
                            content=ft.Text("Мировые данные"),
                            on_click=lambda _: self.open_main_page(),
                        ),

                        ft.MenuItemButton(
                            content=ft.Text("Собственные данные"),
                            on_click=lambda _: self.open_personal_page(),
                        ),
                    ],
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def on_save_result(self, e):
        if self.file_name:
            self.data.save_data(self.file_name, e.path)
            self.file_name = None
    
    def on_upload_result(self, e):
        if self.file_name:
            personal_path = self.uploader.upload_data(self.file_name, e.files[0].path)
            self.personal_data.read_data({self.file_name: personal_path})
            self.file_name = None
            self.update_personal_table()

    def save_data(self, e):
        self.file_name = e.control.data
        self.file_saver.save_file(allowed_extensions=['xlsx'])

    def upload_data(self, e):
        self.file_name = e.control.data
        self.file_uploader.pick_files(allow_multiple=False)

        self.update_personal_table()

    def clear_data(self, e):
        self.personal_data.destroy()
        self.update_personal_table(self)
    
    def open_main_page(self):
        self.controls[-1].visible = False
        self.controls[-2].visible = False
        self.controls[-3].visible = True
        self.page.update()
    
    def open_personal_page(self):
        self.controls[-3].visible = False
        self.controls[-2].visible = True
        self.controls[-1].visible = True
        self.page.update()
    

class Info(Page):    
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page
        self.controls = [
            TitleBar(page),
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
                                    color="white", size=20, text_align="CENTER"
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

