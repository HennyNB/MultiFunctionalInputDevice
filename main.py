import sys

sys.path.append('.\\')


class MultiFunctionalInputDevice(object):

    @staticmethod
    def setting_configs():
        import config

        config = config.Config()
        config.setting_configs()

    @staticmethod
    def total_creator():
        import creator

        creator = creator.Creator()
        creator.total_creator()

    @staticmethod
    def window_settings():
        import console_settings

        console_settings = console_settings.ConsoleSettings()
        console_settings.console_settings()

    @staticmethod
    def information_writer():
        import important_information_writer

        important_information_writer = important_information_writer.ImportantInformationWriter()
        important_information_writer.writer()

    @staticmethod
    def programme():
        import manager

        manager = manager.Manager()
        manager.manager()


def main():
    main_programme = MultiFunctionalInputDevice()

    main_programme.setting_configs()
    main_programme.total_creator()
    main_programme.window_settings()
    main_programme.information_writer()
    main_programme.programme()


if __name__ == '__main__':
    main()
