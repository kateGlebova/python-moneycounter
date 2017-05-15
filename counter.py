class Counter:

    def __init__(self):
        self.operations_list = []

    def load_from_file(self, path):
        import pickle
        f = open(path, 'rb')
        self.operations_list = pickle.load(f)
        f.close()

    def add_operation(self, operation):
        self.operations_list.append(operation)

    def get_operations_by_date(self, date):
        res = list()
        for k in self.operations_list:
            if k.date == date:
                res.append(k)
        return res

    def get_operations_by_description(self, description):
        res = list()
        for k in self.operations_list:
            if k.description == description:
                res.append(k)
        return self.list_to_string(res)

    def get_operations_by_money(self, money):
        res = list()
        for k in self.operations_list:
            if k.money == money:
                res.append(k)
        return self.list_to_string(res)

    def set_operations(self, operations_list):
        self.operations_list = operations_list

    def get_operations(self):
        return self.operations_list

    def get_balance(self):
        balance = 0
        for k in self.operations_list:
            balance += k.get_money()
        return balance

    @staticmethod
    def list_to_string(res):
        s = ""
        if len(res) != 0:
            for k in res:
                s += k.to_string() + "\n"
        else:
            s += "No matches \n"
        return s