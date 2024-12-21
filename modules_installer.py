import os
import sys
import importlib.util

sys.path.append('.\\')
import config
import get_modules


class ModulesInstaller(object):
    config = config.Config()
    get_modules = get_modules.GetModules()

    install_command = 'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple '

    modules_list = get_modules.get_modules()

    def installer_config(self, module: str):
        print('')
        self.config.try_installing_modules(module=module)

        print('')
        os.system(self.install_command + module)

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write('Installed modules successfully ' + self.config.now() + self.config.next + self.config.next)

        print('')

    def installer(self):
        [self.installer_config(module=module)
         for module in self.modules_list
         if importlib.util.find_spec(module) is None]

        os.system('cls')

        self.checker()

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
            self.installer()

        else:
            pass
