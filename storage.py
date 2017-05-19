import storage_yaml
import storage_json
import storage_pickle
import config


class Storage:

    def load_data(self, file):
        data = self.get_file_module(config.AppConfiguration()
                                    .get_configuration("configuration.cfg", "serialization", "type"))
        return data.deserialization(file)

    def save_data(self, file, data):
        f = self.get_file_module(config.AppConfiguration()
                                 .get_configuration("configuration.cfg", "serialization", "type"))
        return f.serialization(file, data)

    @staticmethod
    def get_file_module(file_type):
        if file_type == "pickle":
            return storage_pickle.PickleFormat()
        elif file_type == "json":
            return storage_json.JsonFormat()
        elif file_type == "yaml":
            return storage_yaml.YamlFormat()