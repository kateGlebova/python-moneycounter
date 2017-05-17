import counter
import operation
import datetime


class View:

    def __init__(self):
        pass

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

    def get_new_operation(self):
        """
        This function return new operation by user input.

        :return: new operation object
        """
        desc = input("Enter operation description: ")
        money = int(self.user_input(lambda: input("Enter money =  ")))
        return operation.Operation(self.get_datetime(), desc, money)

    def run(self):
        """
        This function doing something depending on users' choice.
        """
        account = counter.Counter()
        account.load_from_file("database.txt")
        i = 0
        while i != 8:
            i = self.user_input(lambda: input("1 - Show operations history \n"
                                              "2 - Add new operation \n"
                                              "3 - Get operations by money \n"
                                              "4 - Get operation by description \n"
                                              "5 - Get operation by date \n"
                                              "6 - Get balance \n"
                                              "7 - Clear operations history \n"
                                              "8 - Exit \n"))
            if i == 1:
                print(counter.Counter().list_to_string(account.get_operations(), "Empty operations history"))
            elif i == 2:
                account.add_operation(self.get_new_operation())
                account.save_into_file("database.txt")
            elif i == 3:
                print(account.get_operations_by_money(int(self.user_input(lambda: input("Enter money value = ")))))
            elif i == 4:
                print(account.get_operations_by_description(input("Enter description value: ")))
            elif i == 5:
                print(account.get_operations_by_date(self.get_datetime()))
            elif i == 6:
                print("balance = " + str(account.get_balance()))
            elif i == 7:
                account.delete_operations()
            elif i != 8:
                print("Wrong choice, ty again")

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
