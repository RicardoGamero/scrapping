from bs4 import BeautifulSoup
import requests
from models.uf import UF
from utils import web_scrapper
from utils import date_parser


class PageError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UfRepository:
    BASE_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf{}.htm'

    @staticmethod
    def get_ufs(date: str) -> list[UF]:
        try:
            day, month, year = date_parser.validate_date(date_str=date)
            url = UfRepository.BASE_URL.format(year)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            table_rows = web_scrapper.find_table_rows_by_month_and_year(
                soup, month
                )
            reponse = web_scrapper.get_data_from_table_by_day_month_year(
                table_rows=table_rows, search_day=day
                )
            return reponse
        except requests.exceptions.HTTPError:
            raise PageError(message=f"HttpError occurred when try get {url}")
