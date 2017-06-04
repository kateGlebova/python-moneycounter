import pickle


class PickleFormat:
    """
        This class works with pickle file.
        Class has 2 methods:
        1. serialization
        2. deserialization.
        """

    @staticmethod
    def serialization(file, data):
        """
        This method dumps into pickle file.
        :param file: object file.
        :param data: data of operation.
        :return: data
        """
        with file:
            file.write(pickle.dumps(data))
        return data

    @staticmethod
    def deserialization(file):
        """
        This method loads from pickle file.
        :param file: object file.
        :return: list of operations.
        """
        with file:
            return pickle.loads(file.read())