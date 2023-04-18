class UF:
    def __init__(self, date: str, value: float):
        self.date = date
        self.value = value

    def to_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'value': self.value
        }
