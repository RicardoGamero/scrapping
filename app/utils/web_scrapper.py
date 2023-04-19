from bs4 import BeautifulSoup

MONTHS_2_NAME = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre",
    "ANTERIORES": "ANTERIORES",
}


def find_table_rows_by_month_and_year(soup: BeautifulSoup, month):
    month_options = soup.select_one("[id='sel_mes']")
    month_options['value'] = month
    month_table_id = generate_id_table(month=month)
    table_info = soup.select_one(f"[id='{month_table_id}']")
    return table_info.find_all('tr')


def get_data_from_table_by_day_month_year(table_rows, search_day):
    data = {}
    for row in table_rows:
        cells = row.find_all(['th', 'td'])
        day = None
        uf = None
        for row in table_rows[1:]:
            cells = row.find_all(['th', 'td'])
            for cell in cells:
                if cell.strong:
                    day = cell.strong.text
                    if int(day) < 10:
                        day = f"0{day}"
                elif cell.text:
                    uf = cell.text
                    if day is not None and uf is not None:
                        data[day] = uf
                    day = None
                    uf = None
                else:
                    pass
    sorted_ufs = dict(sorted(data.items()))
    return sorted_ufs.get(search_day)


def generate_id_table(month):
    print(MONTHS_2_NAME, month)
    value = f"mes_{MONTHS_2_NAME[month]}"
    return value
