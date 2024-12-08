import os
import sys
import importlib.util

sys.path.append('.\\')
import config
import get_imports


class Installer(object):
    config = config.Config()
    get_imports = get_imports.GetImports()

    install_command = 'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple '

    modules_list = get_imports.get_imports(path='.\\')

    def installer_config(self, module: str):
        print('')
        self.config.try_installing_modules(module=module)

        print('')
        os.system(self.install_command + module)

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write('Installed modules successfully ' + self.config.now() + self.config.next + self.config.next)

    def installer(self):
        [self.installer_config(module=module)
         for module in self.modules_list
         if importlib.util.find_spec(module) is None]
