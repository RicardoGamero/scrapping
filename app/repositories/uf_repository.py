from bs4 import BeautifulSoup
import requests
from models.uf import UF
from utils.web_scrapper import find_table_rows_by_month_and_year
from datetime import datetime


class UfRepository:
    BASE_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf{}.htm'

    @staticmethod
    def get_ufs(year: str, month: str) -> list[UF]:
        url = UfRepository.BASE_URL.format(year)
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        with open("resultado.html", "w") as file:
            file.write(str(soup))
        table_rows = find_table_rows_by_month_and_year(soup, year, month)
        ufs = []
        for row in table_rows:
            date = datetime.strptime(row[0].text, '%d-%m-%Y')
            value = float(row[1].text.replace('.', '').replace(',', '.'))
            ufs.append(UF(date, value))
        return ufs
