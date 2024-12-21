import sys

sys.path.append('.\\')


class MainProgramme(object):

    @staticmethod
    def operator():
        import modules_installer

        installer = modules_installer.ModulesInstaller()
        installer.installer()

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
    def main():
        import manager

        manager = manager.Manager()
        manager.manager()


def main():
    main_programme = MainProgramme()

    main_programme.window_settings()
    main_programme.total_creator()
    main_programme.operator()
    main_programme.information_writer()
    main_programme.main()


if __name__ == '__main__':
    main()
