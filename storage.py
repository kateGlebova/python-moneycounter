import storage_yaml
import storage_json
import storage_pickle
import config


class Storage:

    def load_data(self, file):
        """
        This method load data from file
        :param file: object file.
        """
        data = self.get_file_module(config.AppConfiguration().get_file_type())
        return data.deserialization(file)

    def save_data(self, file, data):
        """
        This method save data to file.
        :param file: object file.
        :param data: data
        """
        f = self.get_file_module(config.AppConfiguration().get_file_type())
        return f.serialization(file, data)

    @staticmethod
    def get_file_module(file_type):
        """
        This method get file module which we choose.
        :param file_type: file type.
        :return: file module
        """
        if file_type == "pickle":
            return storage_pickle.PickleFormat()
        elif file_type == "json":
            return storage_json.JsonFormat()
        elif file_type == "yaml":
            return storage_yaml.YamlFormat()
