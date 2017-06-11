from sqlalchemy.orm import sessionmaker

import counter
import operation
import datetime
import storage
import config
from sqlalchemy import create_engine

from models import Base, Operation, Date


class View:

    def __init__(self):
        self.session = self._init_db()

    def _init_db(self):
        """
        Create a db engine, create tables if they don't exist, create a db session.
        :return: Session | a db session
        """
        engine = create_engine(self.get_database_url())
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)()

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
        date = self.session.query(Date).filter_by(date=date_input).first() or Date(date=date_input)
        return {'date': date,
                'description': desc,
                'money': money}

    def run(self):
        """
        This function doing something depending on users' choice.
        """
        i = 0
        while i != 8:
            i = self.user_input(self.menu_function)
            if i == 1:
                for operation in self.session.query(Operation).all():
                    print(operation)
            elif i == 2:
                self.session.add(Operation(**self.get_new_operation_data()))
                self.session.commit()
            elif i == 3:
                for operation in self.session.query(Operation).filter_by(
                        money=float(self.user_input(self.get_money_function))).all():
                    print(operation)
            elif i == 4:
                for operation in self.session.query(Operation).filter_by(
                        description=self.get_description_function()).all():
                    print(operation)
            elif i == 5:
                for operation in self.session.query(Operation).filter_by(date=self.get_datetime()).all():
                    print(operation)
            elif i == 6:
                print("balance = " + str(Operation.get_balance(self.session)))
            elif i == 7:
                for operation in self.session.query(Operation).all():
                    self.session.delete(operation)
                self.session.commit()
            elif i != 8:
                print("Wrong choice, try again")

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

    def get_database_url(self):
        return 'postgresql://katya:ivan@localhost/account'
