import counter
import operation
import datetime


class View:

    def __init__(self):
        pass

    @staticmethod
    def get_datetime():
        year = int(input("Year = "))
        month = int(input("Month = "))
        day = int(input("Day = "))
        return datetime.datetime(year, month, day)

    def run(self):
        account = counter.Counter()
        account.load_from_file("database.txt")
        i = 0
        while i != 7:
            i = self.user_input()
            if i == 1:
                for k in account.get_operations():
                    print(k.to_string())
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

    @staticmethod
    def user_input():
        return int(input("1 - Show operations history \n"
                         "2 - Add new operation \n"
                         "3 - Get operations by money \n"
                         "4 - Get operation by description \n"
                         "5 - Get operation by date \n"
                         "6 - Get balance \n"
                         "7 - Exit \n"))