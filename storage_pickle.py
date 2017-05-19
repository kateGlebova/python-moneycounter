import pickle


class PickleFormat:

    @staticmethod
    def serialization(file, data):
        with file:
            file.write(pickle.dumps(file))
        return data

    @staticmethod
    def deserialization(file):
        with file:
            return pickle.loads(file.read())