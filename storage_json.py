import datetime
import json
from operation import Operation

class JsonFormat:

    @staticmethod
    def serialization(file, data):
        with file:
            json.dump([i.__dict__() for i in data], file)
        return data

    @staticmethod
    def deserialization(file):
        with file:
            return [Operation(datetime.datetime(i["year"], i["month"], i["day"]), i["description"], i["money"]) for i in json.loads(file.read())]