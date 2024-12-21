import sys

sys.path.append('.\\')
import modules_installer
import get_modules


class Checker(object):
    installer = modules_installer.Installer()
    get_modules = get_modules.GetModules()

    modules_list = get_modules.get_modules()

    def writer(self):
        open_file = '.\\importer.py'
        modules = ('import' + ' ') + ('\n' + 'import' + ' ').join(self.modules_list) + '\n'

        with open(file=open_file, mode='r', encoding='UTF-8') as file:
            content = file.read()

        if not content == modules:
            with open(file=open_file, mode='w', encoding='UTF-8') as file:
                file.write(modules)

    def checker(self):
        self.writer()

        try:
            import importer

        except ModuleNotFoundError or ImportError:
            self.installer.installer()

        else:
            pass
