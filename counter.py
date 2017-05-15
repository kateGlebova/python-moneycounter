class Counter:
    """This class implements simple money accounter.
           You can use it for storing notes about your income and
           outcome, search notes and group them by their attributes."""
    def __init__(self):
        """
        Create new Counter object from existing DataFrame.
        >>> print(Counter())
        List of notes is empty

        """
        self.operations_list = []

    def load_from_file(self, path):
        '''

        :param path:
        :return:
        '''
        import pickle
        f = open(path, 'rb')
        self.operations_list = pickle.load(f)
        f.close()

    def save_into_file(self, path):
        import pickle
        f = open(path, 'wb')
        pickle.dump(self.get_operations(), f)
        f.close()

    def add_operation(self, operation):
        """This function add operation
        :param operation:
        :type operation:
        :return: nothing
        """
        self.operations_list.append(operation)


    def get_operations_by_date(self, date):
        """
        This function allow get operations by date
        :param date: the date of operation
        :type date: date
        :return: list of operations by date
        :rtype: string
        """
        res = list()
        for k in self.operations_list:
            if k.date.date() == date.date():
                res.append(k)
        return self.list_to_string(res)

    def get_operations_by_description(self, description):
        """
        This function allow get operations by description
        :param description: the description of operation
        :type description: string
        :return: list of operations by description
        :rtype: string
        """
        res = list()
        for k in self.operations_list:
            if k.description == description:
                res.append(k)
        return self.list_to_string(res)

    def get_operations_by_money(self, money):
        """
        This function allow get operations by money
        :param money: amount money of operation
        :type money: float
        :return: list of operations by money
        :rtype: string
        """
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()