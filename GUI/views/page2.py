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
    countryNames = []
    countryRates = []
    srDobs = []
    dnDobs = []
    bar_labels = []
    bar_colors = []

    # DEFINE INPUT FIELDS
    date = TextField(label="date")
    price = TextField(label="price")
    usdRub = TextField(label="usd rub")
    countryName = TextField(label="country name")
    countryRate = TextField(label="country rate")
    srDob = TextField(label="Среднедневная добыча")
    dnDob = TextField(label="Дневная добыча")

    # FUNCTION TO CREATE CHART
    def create_chart(fig, ax):
        ax.bar(dates, barrelPrice, label=bar_labels, color=bar_colors)
        ax.set_ylabel("dates Data")
        ax.set_title("dates Data Visualization")
        ax.legend(title="dates Details")


    mytable = DataTable(
        columns=[
            DataColumn(Text("date")),
            DataColumn(Text("price")),
            DataColumn(Text("usd rub")),
            DataColumn(Text("country name")),
            DataColumn(Text("rating")),
            DataColumn(Text("sr dob")),
            DataColumn(Text("dn dob")),
        ],
        rows=[]
    )
    # FUNCTION TO ADD DATA AND UPDATE CHART
    def add_new_data(e):
        try:
            mytable.rows.append(
			DataRow(
				cells=[
				DataCell(Text(date.value)),
				DataCell(Text(price.value)),
                DataCell(Text(usdRub.value)),
				DataCell(Text(countryName.value)),
                DataCell(Text(countryRate.value)),
				DataCell(Text(srDob.value)),
                DataCell(Text(dnDob.value)),
				]
				)
			)

            # UPDATE CHART DATA
            dates.append(date.value)
            barrelPrice.append(price.value)
            course.append(usdRub.value)
            countryNames.append(countryName.value)
            countryRates.append(countryRate.value)
            srDobs.append(srDob.value)
            dnDobs.append(dnDob.value)

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
            date,
            price,
            usdRub,
            countryName,
            countryRate,
            srDob,
            dnDob,
            Row(
                [
                    ElevatedButton("Add Data", on_click=add_new_data),
                    ElevatedButton("Open Chart", on_click=open_chart),
                ]
            ),
            mytable,
            ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ElevatedButton("print", on_click=lambda _: print(dates, barrelPrice, course, countryNames, countryRates, srDobs, dnDobs))
        ]
    )