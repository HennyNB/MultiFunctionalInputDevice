import os
import sys

sys.path.append('.\\')
import config
import get_modules


class ModulesInstaller(object):
    config = config.Config()
    get_modules = get_modules.GetModules()

    file = '.\\' + 'requirements.txt'

    create_file_command = 'pip freeze > ' + file
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

    @staticmethod
    def find_file(filename: str):
        path_list = os.listdir('.\\')
        return [it for it in path_list if filename in it][0]

    def installer(self):
        modules_list = []

        os.system(self.create_file_command)

        with open(file=self.file, mode='r', encoding='UTF-8') as file:
            line_content = file.readlines()

        os.remove(self.file)

        [modules_list.append(item.split('==')[0]) for item in line_content]

        for module in self.modules_list:
            if module not in modules_list:
                self.installer_config(module=module)

                if module == self.modules_list[-1]:
                    os.system('start ' + self.find_file(filename='main'))
                    sys.exit()
