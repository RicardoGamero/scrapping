from datetime import date


def parse_date(date_str: str) -> date:
    year, month, day = map(int, date_str.split('-'))
    return date(year, month, day)
