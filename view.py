import counter
import operation
import datetime
import view


class View:

    def __init__(self):
        pass

    @staticmethod
    def get_datetime():
        """
        user input year, month, day to get operations by date
        
        :return: datetime - year, month, day
        :rtype: date
        """
        year = int(input("Year = "))
        month = int(input("Month = "))
        day = int(input("Day = "))
        return datetime.datetime(year, month, day)

    def run(self):
        """
        this function return result depending on users' choice
        
        """
        account = counter.Counter()
        account.load_from_file("database.txt")
        i = 0
        while i != 8:
            i = self.user_input()
            if i == 1:
                print(counter.Counter().list_to_string(account.get_operations(), "Empty operations history"))
            elif i == 2:
                desc = input("Enter operation description: ")
                money = int(input("Enter money =  "))
                account.add_operation(operation.Operation(self.get_datetime(), desc, money))
                account.save_into_file("database.txt")
            elif i == 3:
                i = int(input("Enter money value = "))
                print(account.get_operations_by_money(i))
            elif i == 4:
                i = input("Enter description value: ")
                print(account.get_operations_by_description(i))
            elif i == 5:
                print(account.get_operations_by_date(self.get_datetime()))
            elif i == 6:
                print("balance = " + str(account.get_balance()))
            elif i == 7:
                account.delete_operations()
            elif i != 8:
                print("Wrong choice, ty again")

    @staticmethod
    def user_input():
        """
        
        this function return numbers of operations available for user
        :return: digit of operation for user
        
        """
        return int(input("1 - Show operations history \n"
                         "2 - Add new operation \n"
                         "3 - Get operations by money \n"
                         "4 - Get operation by description \n"
                         "5 - Get operation by date \n"
                         "6 - Get balance \n"
                         "7 - Exit \n"))