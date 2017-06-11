import datetime


class View:
    def get_datetime(self):
        """
        User input year, month, day to get operations by date.

        :return: datetime - year, month, day
        :rtype: date
        """
        year = int(self.user_input(lambda: input("Year = ")))
        month = int(self.user_input(lambda: input("Month = ")))
        day = int(self.user_input(lambda: input("Day = ")))
        return datetime.datetime(year, month, day)

    @staticmethod
    def get_money_function():
        return input("Enter money value = ")

    @staticmethod
    def get_description_function():
        return input("Enter operation description: ")

    def get_new_operation_data(self):
        """
        This function return new operation by user input.

        :return: new operation object
        """
        desc = self.get_description_function()
        money = float(self.user_input(self.get_money_function))
        date_input = self.get_datetime()
        return {'date': date_input,
                'description': desc,
                'money': money}

    @staticmethod
    def menu_function():
        return input("1 - Show operations history \n"
                     "2 - Add new operation \n"
                     "3 - Get operations by money \n"
                     "4 - Get operation by description \n"
                     "5 - Get operation by date \n"
                     "6 - Get balance \n"
                     "7 - Clear operations history \n"
                     "8 - Exit \n")

    @staticmethod
    def user_input(input_func=input):
        """
        This function return numbers of operations available for user.
        :return: digit of operation for user
        :Example
        >>> import view
        >>> view.View().user_input(lambda: 'k')
        -1
        """
        try:
            return int(input_func())
        except ValueError:
            return -1
