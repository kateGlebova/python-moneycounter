class AppConfiguration:
    """
        This class works with file type.
        Class has two methods:
        1. get_file_type
        2. set_file_type.
        """

    # Name of configuration file.
    file_name = "configuration.cfg"

    # Name of serialization section for configuration file.
    serial_section = "serialization"

    # Field for save file type for configuration file.
    serial_type = "type"

    def get_file_type(self):
        """
        This method get file type.
        :return: file type of serialization.
        """
        import configparser
        config = configparser.RawConfigParser()
        config.read(self.file_name)
        return config.get(self.serial_section, self.serial_type)

    def set_file_type(self, value):
        """
        This method set file type.
        :param value: file type.
        :return: nothing.
        """
        import configparser
        config = configparser.RawConfigParser()
        config.read(self.file_name)
        config.set(self.serial_section, self.serial_type, value)
        with open(self.file_name, 'w') as f:
            config.write(f)
