import io
import unittest
import counter
import config
import storage


class StringTest(unittest.TestCase):

    test_data = [{"data": "16 May 2017", "description": "donate1", "money": 100},
                 {"data": "16 May 2017", "description": "donate2", "money": 100},
                 {"data": "16 May 2017", "description": "donate3", "money": 100},
                 {"data": "16 May 2017", "description": "donate4", "money": 100},
                 {"data": "16 May 2017", "description": "donate5", "money": 100}]

    def test_pickle_format(self):
        import pickle

        # test load
        config.AppConfiguration().set_file_type("pickle")
        self.assertEqual(self.test_data, storage.Storage().load_data(io.BytesIO(pickle.dumps(self.test_data))))

        # test save
        config.AppConfiguration().set_file_type("pickle")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.BytesIO(), self.test_data))

    def test_json_format(self):
        import json

        # test load
        file = io.StringIO(json.dumps(self.test_data))
        config.AppConfiguration().set_file_type("json")
        self.assertEqual(self.test_data, storage.Storage().load_data(file))

        # test save
        config.AppConfiguration().set_file_type("json")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.StringIO(), self.test_data))

    def test_yaml_format(self):
        import yaml

        # test load
        file = io.StringIO(yaml.dump(self.test_data))
        config.AppConfiguration().set_file_type("yaml")
        self.assertEqual(self.test_data, storage.Storage().load_data(file))

        # test save
        config.AppConfiguration().set_file_type("yaml")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.StringIO(), self.test_data))