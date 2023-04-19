from datetime import date, datetime


def validate_date(date_str: str) -> date:
    error_msg = "Error occurred while validating date"
    try:
        date = datetime.strptime(date_str, '%d-%m-%Y')
        min_date = datetime.strptime('01-01-2013', '%d-%m-%Y')
        max_date = datetime.now().replace(day=1)
        if min_date <= date <= max_date:
            return parse_date(date_str)
        else:
            error_msg = "Error the date it's not validate"
            raise
    except Exception:
        raise ValueError(error_msg)


def parse_date(date_str: str) -> date:
    day, month, year = date_str.split('-')
    return day, month, year
