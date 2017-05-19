import yaml


class YamlFormat:

    @staticmethod
    def serialization(file, data):
        with file:
            yaml.dump(data, file)
        return data

    @staticmethod
    def deserialization(file):
        with file:
            return yaml.load(file.read())