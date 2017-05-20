class AppConfiguration:

    #
    file_name = "configuration.cfg"

    #
    serial_section = "serialization"

    #
    serial_type = "type"

    def get_file_type(self):
        import configparser
        config = configparser.RawConfigParser()
        config.read(self.file_name)
        return config.get(self.serial_section, self.serial_type)

    def set_file_type(self, value):
        import configparser
        config = configparser.RawConfigParser()
        config.read(self.file_name)
        config.set(self.serial_section, self.serial_type, value)
        try:
            with open(self.file_name, 'w') as f:
                config.write(f)
        except FileNotFoundError:
            print("FileNotFound")