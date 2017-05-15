import datetime

import operation


class Operation(object):
    """
    Operation encapsulates a date, description and money
    """

    def __init__(self, date, description, money):
        """
        Constructor a new 'Operation' object

        :param date: The date of Operation
        :param description: The description of Operation
        :param money: The money of Operation

        """
        self.date = date
        self.description = description
        self.money = money

    def set_date(self, date):
        """
        This function set the date

        :param date: The date of Operation
        :type date: date
        :return: Nothing
        """
        self.date = date

    def set_description(self, description):
        """
        This function set the description

        :param description: The description of Operation
        :type description: String
        :return: Nothing
        """
        self.description = description

    def set_money(self, money):
        """
        This function set the money of Operation

        :param money: The money of Operation
        :type money: float
        :return: Nothing
        """
        self.money = money

    def get_date(self):
        """
        This function get the date of Operation
        
        :return: The date of Operation
        :rtype: date
        
        :Example.
        >>> operation.Operation(datetime.datetime(2000, 2, 2), "donate", 150).get_date()
        datetime.datetime(2000, 2, 2, 0, 0)
        """
        return self.date

    def get_description(self):
        """
        This function  get description of Operation
        
        :return: The description of Operation
        :rtype: String
        
        :Example
        >>> operation.Operation(datetime.datetime.today(), "donate", 150).get_description()
        'donate'
        """
        return self.description

    def get_money(self):
        """
        This function get money of Operation
        
        :return: The money of Operation
        :rtype: float
        
        :Example
        >>> operation.Operation(datetime.datetime.today(), "donate", 150).get_money()
        150
        """
        return self.money

    def to_string(self):
        """
        This function convert the date, description and money to String
        
        :return: String of date, money and description
        :rtype: String

        :Example
        >>>
        """
        return self.date.strftime('%d %b %Y: ') + "\t" + self.description + "\t" + str(self.money)

