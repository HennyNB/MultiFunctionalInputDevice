import os
import sys
import importlib.util

sys.path.append('.\\')
import config


class Control(object):
    config = config.Config()

    install_command = 'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple '

    ordinary_install_modules_list = ['pyautogui', 'requests']
    extraordinary_install_modules_list = [['', '']]

    module_list = []

    event_list = ['']

    def control(self):
        self.installer()
        self.checker()

        os.system('cls')

    def installer_config(self, module: str):
        print('')
        self.config.try_installing_modules(module=module)

        print('')
        os.system(self.install_command + module)

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write('Installed modules successfully ' + self.config.now() + '\n' + '\n')

    def installer(self):
        [[self.installer_config(module=group[0])
          for group in
          [item for item in self.extraordinary_install_modules_list]
          if importlib.util.find_spec(group[1]) is None]
         for item in self.extraordinary_install_modules_list
         if not item[0] in self.event_list or not item[1] in self.event_list]

        [self.installer_config(module=module)
         for module in self.ordinary_install_modules_list
         if importlib.util.find_spec(module) is None]

    def checker(self):
        try:
            self.settings()

        except ModuleNotFoundError or ImportError:
            self.installer()

        else:
            self.settings()

    @staticmethod
    def settings():
        import console_settings

        console_settings = console_settings.ConsoleSettings()
        console_settings.console_settings()
