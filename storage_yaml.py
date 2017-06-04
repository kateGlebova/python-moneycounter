import yaml


class YamlFormat:
    """
    This class works with yaml file.
    Class has 2 methods:
    1. serialization
    2. deserialization.
    """

    @staticmethod
    def serialization(file, data):
        """
        This method dumps into yaml file.
        :param file: object file.
        :param data: data of operation.
        :return: data
        """
        with file:
            yaml.dump(data, file)
        return data

    @staticmethod
    def deserialization(file):
        """
        This method loads from yaml file.
        :param file: object file.
        :return: list of operations.
        """
        with file:
            return yaml.load(file.read())