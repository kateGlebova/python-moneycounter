import datetime
import json
from operation import Operation


class JsonFormat:
    """
    This class works with json file.
    Class has 2 methods:
    1. serialization
    2. deserialization.
    """

    @staticmethod
    def serialization(file, data):
        """
        This method dumps into json file.
        :param file: object file.
        :param data: data of operation.
        :return: data
        """
        with file:
            json.dump([i.get_json() for i in data], file)
        return data

    @staticmethod
    def deserialization(file):
        """
        This method loads from json file.
        :param file: object file.
        :return: list of operations.
        """
        with file:
            return [Operation(datetime.datetime(i["year"], i["month"],
                                                i["day"]), i["description"],
                              i["money"]) for i in json.loads(file.read())]
