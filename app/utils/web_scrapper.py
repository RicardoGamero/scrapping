import requests
from bs4 import BeautifulSoup


def find_table_rows_by_month_and_year(soup: BeautifulSoup, year, month):
    print("entrando ", month)
    year_options = soup.select_one("[id='sel_anyo']")
    print(year_options)
    month_options = soup.select_one("[id='sel_mes']")
    month_options['value'] = month
    with open("resultado3.html", "w") as file:
        file.write(str(soup))
    response = requests.get(url='https://www.sii.cl/valores_y_fechas/uf/uf2021.htm')
    html = response.content
    _soup = BeautifulSoup(html, 'html.parser')
    with open("resultado2.html", "w") as file:
        file.write(str(_soup))
    month_dropdown = soup.select_one("#my-wrapper>div.web-sii.cuerpo>div>div>div>div.col-sm-9.contenido>div.filtro>div>div.col-sm-5>div>select")

    #print(month_dropdown)
    #print(example)
    year_dropdown = soup.select_one(
        "#my-wrapper>div.web-sii.cuerpo>div>div>div>div.col-sm-9.contenido>div.filtro>div>div.col-sm-3>div"
        )
    #print(year_dropdown)
    if not month_dropdown or not year_dropdown:
        return []

    month_options = month_dropdown.find_all('option')
    #print("month_options")
    #print(month_options)
    year_options = year_dropdown.find_all('option')
    #print("year_options")
    #print(year_options)
    month_dict = {
        option.text.lower(): option['value'] for option in month_options
        }
    year_dict = {option.text: option['value'] for option in year_options}
    month_value = month_dict.get(month.lower())
    year_value = year_dict.get(year)
    if not month_value or not year_value:
        return []
    table_id = 'UF{}{}'.format(year_value, month_value)
    table = soup.find('table', {'id': table_id})
    if not table:
        return []
    return table.tbody.find_all('tr')
