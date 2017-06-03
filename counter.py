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

    def __iter__(self):
        self.iter = self.operations_list
        return self

    def __next__(self):
        if self.iter:
            head = self.iter[0]
            self.iter = self.iter[1:]
            return head
        else:
            raise StopIteration

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
        >>> import operation
        >>> account = counter.Counter()
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", 100))
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", -100))
        >>> account.add_operation(operation.Operation(datetime.datetime.today(), "donate", 100))
        >>> account.get_operations_by_date(datetime.datetime(2016, 12, 12))
        'No matches \\n'
        """
        return [k for k in self.operations_list if k.get_date().date() == date.date()]

    def get_operations_by_description(self, description):
        """
        This function allow get operations by description
        :param description: the description of operation
        :type description: string
        :return: list of operations by description
        :rtype: string
        :Example
        >>> import counter
        >>> import operation
        >>> import datetime
        >>> account = counter.Counter()
        >>> account.add_operation(operation.Operation(datetime.datetime(2017, 5, 20), "donate1", 100))
        >>> account.add_operation(operation.Operation(datetime.datetime(2017, 5, 20), "donate2", -100))
        >>> account.add_operation(operation.Operation(datetime.datetime(2017, 5, 20), "donate1", 100))
        >>> account.get_operations_by_description("donate1")
        '20 May 2017:\\tdonate1\\t100\\n20 May 2017:\\tdonate1\\t100\\n'
        """
        return [k for k in self.operations_list if k.get_description() == description]

    def get_operations_by_money(self, money):
        """
        This function allow get operations by money
        :param money: amount money of operation
        :type money: float
        :return: list of operations by money
        :rtype: string
        :Example
        >>> import counter
        >>> import operation
        >>> import datetime
        >>> account = counter.Counter()
        >>> account.add_operation(operation.Operation(datetime.datetime(2017, 5, 20), "donate1", 100))
        >>> account.get_operations_by_money(150)
        'No matches \\n'
        """
        return [k for k in self.operations_list if k.get_money() == money]

    def get_operations(self):
        """
        This function get operations
        :return: list of operations
        :rtype: operations list
        """
        return self.operations_list

    def set_operations(self, data):
        self.operations_list = data

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
