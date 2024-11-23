import os
import sys
import datetime
import importlib.util

sys.path.append('.\\')
import config


class Control(object):

    def __init__(self):
        self.console_settings = None

        self.config = config.Config()

        self.now = str(datetime.datetime.now())

        self.install_command = 'pip install '
        self.install_mode = ' -i '
        self.install_url = 'https://pypi.tuna.tsinghua.edu.cn/simple'

        self.installed_modules_successful = 'Installed modules '

        self.ordinary_install_modules_list = ['pyautogui', 'tqdm', 'requests']
        self.extraordinary_install_modules_list = ['pypiwin32', 'win32']

        self.total = self.installed_modules_successful + self.now + '\n'

    def control(self):
        [self.ordinary_installer(module=module)
         for module in self.ordinary_install_modules_list]

        self.settings()
        os.system('cls')

    def installer_config(self, module):
        os.system(self.install_command + module + self.install_mode + self.install_url)

    def extraordinary_installer(self):
        if importlib.util.find_spec(self.extraordinary_install_modules_list[1]) is None:
            self.installer_config(self.extraordinary_install_modules_list[0])

    def ordinary_installer(self, module):
        if importlib.util.find_spec(module) is None:
            print('')
            self.config.try_installing_modules(module=module)

            print('')
            self.installer_config(module=module)

    def settings(self):
        [self.installer_config(module=module)
         for module in self.ordinary_install_modules_list
         if importlib.util.find_spec(module) is None]

        if importlib.util.find_spec(self.extraordinary_install_modules_list[1]) is not None:
            import console_settings

            self.console_settings = console_settings.ConsoleSettings()
            self.console_settings.console_settings()

        else:
            self.installer_config(module=self.extraordinary_install_modules_list[0])
