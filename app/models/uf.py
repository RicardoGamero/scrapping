class UF:
    def __init__(self, date: str, value: float):
        self.date = date
        self.value = value

    def to_dict(self):
        return {
            'date': self.date,
            'value': self.value
        }
