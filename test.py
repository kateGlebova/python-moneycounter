import io
import unittest
import counter
import config
import storage


class StringTest(unittest.TestCase):
    """
    In this class we test file formats.
    Class has three functions:
    1. test_pickle_format.
    2. test_json_format.
    3. test_yaml_format.
    """

    test_data = [{"data": "16 May 2017", "description": "donate1", "money": 100},
                 {"data": "16 May 2017", "description": "donate2", "money": 100},
                 {"data": "16 May 2017", "description": "donate3", "money": 100},
                 {"data": "16 May 2017", "description": "donate4", "money": 100},
                 {"data": "16 May 2017", "description": "donate5", "money": 100}]

    def test_pickle_format(self):
        """
        This function tests pickle file.
        :return: nothing.
        """
        import pickle

        # test load
        config.AppConfiguration().set_file_type("pickle")
        self.assertEqual(self.test_data, storage.Storage().load_data(io.BytesIO(pickle.dumps(self.test_data))))

        # test save
        config.AppConfiguration().set_file_type("pickle")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.BytesIO(), self.test_data))

    def test_json_format(self):
        """
        This function tests json file.
        :return: nothing
        """
        import json

        # test load
        file = io.StringIO(json.dumps(self.test_data))
        config.AppConfiguration().set_file_type("json")
        self.assertEqual(self.test_data, storage.Storage().load_data(file))

        # test save
        config.AppConfiguration().set_file_type("json")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.StringIO(), self.test_data))

    def test_yaml_format(self):
        """
        This function tests yaml file.
        :return: nothing.
        """
        import yaml

        # test load
        file = io.StringIO(yaml.dump(self.test_data))
        config.AppConfiguration().set_file_type("yaml")
        self.assertEqual(self.test_data, storage.Storage().load_data(file))

        # test save
        config.AppConfiguration().set_file_type("yaml")
        self.assertEqual(self.test_data, storage.Storage().save_data(io.StringIO(), self.test_data))