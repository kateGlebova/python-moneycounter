from configparser import ConfigParser
from os.path import join, dirname
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import view
from models import Base, Operation, Date


class Controller:
    _config_path = join(dirname(__file__), 'configuration.cfg')

    def __init__(self):
        self.config = self._get_config()
        self.session = self._get_db_session()
        self.view = view.View()

    def _get_db_session(self):
        """
        Create a db engine, create tables if they don't exist, create a db session.
        :return: Session | a db session
        """
        engine = create_engine(self.get_database_url())
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)()

    def _get_config(self):
        """
        Get the config object from the config file.
        """
        config = ConfigParser()
        config.read(self._config_path)
        return config

    def get_database_url(self):
        """
        Get database url from the config file.
        :return:
        """
        database = self.config['database']['type']
        try:
            return self.config[database]['db_url']
        except KeyError:
            raise Exception('%s engine is not supported.' % database)

    def run(self):
        """
        This function doing something depending on users' choice.
        """
        i = 0
        while i != 8:
            i = self.view.user_input(self.view.menu_function)
            if i == 1:
                for operation in self.session.query(Operation).all():
                    print(operation)
            elif i == 2:
                new_operation = self.view.get_new_operation_data()
                new_operation['date'] = self.session.query(Date).filter_by(date=new_operation['date']).first() or \
                                        Date(date=new_operation['date'])
                self.session.add(Operation(**new_operation))
                self.session.commit()
            elif i == 3:
                for operation in self.session.query(Operation).filter_by(
                        money=float(self.view.user_input(self.view.get_money_function))).all():
                    print(operation)
            elif i == 4:
                for operation in self.session.query(Operation).filter_by(
                        description=self.view.get_description_function()).all():
                    print(operation)
            elif i == 5:
                for operation in self.session.query(Operation).filter_by(
                        date=self.session.query(Date).filter_by(date=self.view.get_datetime()).first()
                ).all():
                    print(operation)
            elif i == 6:
                print("Balance = %.2f" % Operation.get_balance(self.session))
            elif i == 7:
                for operation in self.session.query(Operation).all():
                    self.session.delete(operation)
                self.session.commit()
            elif i != 8:
                print("Wrong choice, try again")


if __name__ == "__main__":
    Controller().run()
