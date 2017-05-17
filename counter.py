class Counter:
    """This class implements simple money counter.
        You can use it for storing notes about your income and
        outcome, search notes and group them by their attributes."""
    def __init__(self):
        """
        Create new Counter object from existing DataFrame.
        List of notes is empty

        """
        self.operations_list = []

    def load_from_file(self, path):
        """
        This function load list of operations from file
        :param path: path of the file
        :type path: string
        :return: nothing
        """
        import pickle
        f = open(path, 'rb')
        self.operations_list = pickle.load(f)
        f.close()

    def save_into_file(self, path):
        """This function save operations into file
        :param path: path of the file
        :type path: string
        :return: nothing
        """
        import pickle
        f = open(path, 'wb')
        pickle.dump(self.get_operations(), f)
        f.close()

    def add_operation(self, operation):
        """This function add operation
        :param operation: operation
        :type operation: Operation
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
        :Example
        >>> import counter
        >>> import datetime
        >>> account = counter.Counter()
        >>> account.load_from_file("database.txt")
        >>> account.get_operations_by_date(datetime.datetime.today())
        'No matches \\n'
        """
        res = list()
        for k in self.operations_list:
            if k.get_date().date() == date.date():
                res.append(k)
        return self.list_to_string(res, "No matches")

    def get_operations_by_description(self, description):
        """
        This function allow get operations by description
        :param description: the description of operation
        :type description: string
        :return: list of operations by description
        :rtype: string
        :Example
        >>> import counter
        >>> account = counter.Counter()
        >>> account.load_from_file("database.txt")
        >>> account.get_operations_by_description("donate")
        '07 May 2017: \\tdonate\\t100\\n07 May 2017: \\tdonate\\t100\\n07 May 2017: \\tdonate\\t100\\n'
        """
        res = list()
        for k in self.operations_list:
            if k.get_description() == description:
                res.append(k)
        return self.list_to_string(res, "No matches")

    def get_operations_by_money(self, money):
        """
        This function allow get operations by money
        :param money: amount money of operation
        :type money: float
        :return: list of operations by money
        :rtype: string
        :Example
        >>> import counter
        >>> account = counter.Counter()
        >>> account.load_from_file("database.txt")
        >>> account.get_operations_by_money(150)
        'No matches \\n'
        >>> account.get_operations_by_money(500.2)
        '07 May 2017: \\tplus\\t500.2\\n'
        """
        res = list()
        for k in self.operations_list:
            if k.money == money:
                res.append(k)
        return self.list_to_string(res, "No matches")

    def get_operations(self):
        """
        This function get operations
        :return: list of operations
        :rtype: operations list
        """
        return self.operations_list

    def delete_operations(self):
        """
        This function delete all operations from list.
        :Example
        >>> import counter
        >>> import operation
        >>> import datetime
        >>> account = counter.Counter()
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", 100))
        >>> account.delete_operations()
        >>> counter.Counter().list_to_string(account.get_operations(), "Empty list")
        'Empty list \\n'
        """
        self.operations_list.clear()

    def get_balance(self):
        """
        This function get balance of operation.
        :return: balance
        :rtype: float
        :Example
        >>> import counter
        >>> import operation
        >>> import datetime
        >>> account = counter.Counter()
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", 100))
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", -100))
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", 100))
        >>> account.get_balance()
        100
        """
        balance = 0
        for k in self.operations_list:
            balance += k.get_money()
        return balance

    @staticmethod
    def list_to_string(res, mes):
        """
        This function convert list to string
        :return: string of result
        :rtype: string
        :Example
        >>> import counter
        >>> account = counter.Counter()
        >>> counter.Counter().list_to_string(account.get_operations(), "No matches")
        'No matches \\n'
        """
        s = ""
        if len(res) != 0:
            for k in res:
                s += k.to_string() + "\n"
        else:
            s += mes + " \n"
        return s
