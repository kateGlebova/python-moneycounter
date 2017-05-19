class AppConfiguration:

    @staticmethod
    def get_configuration(file_name, section, option):
        import configparser
        config = configparser.RawConfigParser()
        config.read(file_name)
        return config.get(section, option)

    @staticmethod
    def set_configuration(file_name, section, option, value):
        import configparser
        config = configparser.RawConfigParser()
        config.read(file_name)
        config.set(section, option, value)
        try:
            with open(file_name, 'w') as f:
                config.write(f)
        except FileNotFoundError:
            print("FileNotFound")