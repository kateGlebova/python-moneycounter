import json


class JsonFormat:

    @staticmethod
    def serialization(file, data):
        with file:
            json.dump(data, file)
        return data

    @staticmethod
    def deserialization(file):
        with file:
            return json.loads(file.read())