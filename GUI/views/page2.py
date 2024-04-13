from flet import *
from flet_route import Params, Basket
import matplotlib
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors
from flet.matplotlib_chart import MatplotlibChart
matplotlib.use("svg")


def Page2(page: Page, params: Params = {}, basket: Basket = {}):

    # DATA VARIABLES FOR CHART
    dates = [] # здесь хранятся значения дат
    barrelPrice = []  # здесь хранятся значения цены за баррель
    course = []
    countryName = []
    countryRate = []
    srDob = []
    dnDob = []
    bar_labels = []
    bar_colors = []

    # DEFINE INPUT FIELDS
    nametxt = TextField(label="Name")
    salarytxt = TextField(label="Salary")
    iqtxt = TextField(label="IQ")
    lengthtxt = TextField(label="Length")
    beavertxt = TextField(label="Beaver")
    srdob = TextField(label="Среднедневная добыча")
    dndob = TextField(label="Дневная добыча")

    # FUNCTION TO CREATE CHART
    def create_chart(fig, ax):
        ax.bar(dates, barrelPrice, label=bar_labels, color=bar_colors)
        ax.set_ylabel("dates Data")
        ax.set_title("dates Data Visualization")
        ax.legend(title="dates Details")

    # FUNCTION TO ADD DATA AND UPDATE CHART
    def add_new_data(e):
        try:
            # Validate and convert input to integers
            salary = int(salarytxt.value)
            iq = int(iqtxt.value)
            length = int(lengthtxt.value)

            # ADD DATA TO TABLE
            mytable.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(nametxt.value)),
                        DataCell(Text(str(salary))),  # Convert back to string for display
                        DataCell(Text(str(iq))),
                        DataCell(Text(str(length))),
                        DataCell(Text(beavertxt.value)),
                        DataCell(Text(srdob.value)),
                        DataCell(Text(dndob.value)),
                    ]
                )
            )

            # UPDATE CHART DATA
            dates.append(nametxt.value)
            barrelPrice.append(salary)

            # GENERATE RANDOM BAR COLORS
            colors = ['purple', 'red', 'pink', 'green', 'blue', 'orange']
            bar_random_color = random.choice(colors)
            bar_labels.append(bar_random_color)
            mycolor = mcolors.to_rgba("tab:" + bar_random_color)
            bar_colors.append(mycolor)

            # CLEAR AND UPDATE CHART
            fig.clear()
            create_chart(fig, ax)
            page.update()

            # SHOW SUCCESS SNACKBAR
            page.snack_bar = SnackBar(
                Text("Информация была успешно добавлена!", size=30), bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()

        except ValueError:
            # Display error message if input is not valid integer
            page.snack_bar = SnackBar(
                Text("Ошибка: Пожалуйста, введите целочисленные значения зп, IQ, и длины.", size=30),
                bgcolor="red",
            )
            page.snack_bar.open = True
            page.update()

    # CREATE FIGURE AND AXES FOR CHART
    fig, ax = plt.subplots()
    create_chart(fig, ax)

    # CREATE DIALOG FOR CHART
    chartdialog = AlertDialog(
        content=MatplotlibChart(fig, expand=True)
    )

    # CREATE TABLE WITH NEW COLUMNS
    mytable = DataTable(
        columns=[
            DataColumn(Text("Name")),
            DataColumn(Text("Salary")),
            DataColumn(Text("IQ")),
            DataColumn(Text("Length")),
            DataColumn(Text("Beaver")),
            DataColumn(Text("srdob")),
            DataColumn(Text("dndob")),
        ],
        rows=[],
    )

    def open_chart(e):
        page.dialog = chartdialog
        chartdialog.open = True
        page.update()

    # Fix indentation here

    return View(
        "/page2/:name2",
        scroll=True,
        controls=[
            Text("Ваши данные"),
            nametxt,
            salarytxt,
            iqtxt,
            lengthtxt,
            beavertxt,
            srdob,
            dndob,
            Row(
                [
                    ElevatedButton("Add Data", on_click=add_new_data),
                    ElevatedButton("Open Chart", on_click=open_chart),
                ]
            ),
            mytable,
            ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ElevatedButton("print", on_click=lambda _: print(dates, barrelPrice, bar_labels))
        ]
    )
