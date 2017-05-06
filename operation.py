class Operation:

    def __init__(self, date, description, money):
        self.date = date
        self.description = description
        self.money = money

    def print_operation(self):
        print(self.date.strftime('%d %b %Y: ') + "\t" + self.description + "\t" + str(self.money))

    def set_date(self, date):
        self.date = date

    def set_description(self, description):
        self.description = description

    def set_money(self, money):
        self.money = money

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def get_money(self):
        return self.money