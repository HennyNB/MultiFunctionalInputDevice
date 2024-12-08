import os
import sys
import ctypes


sys.path.append('.\\')
import config


class ConsoleSettings(object):
    config = config.Config()

    ctypes_handle = ctypes.windll.kernel32.GetStdHandle(-10)

    @staticmethod
    def get_screen():
        screen = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]
        return screen

    def console_settings(self):
        os.system('title ' + self.config.window_title)
        os.system('color 0F')
        os.system('mode con cols=' + str(self.config.split_quantity) + ' lines=15')

        self.enable_quick_edit_mode()

    def enable_quick_edit_mode(self):
        mode = ctypes.c_ulong()

        ctypes.windll.kernel32.GetConsoleMode(self.ctypes_handle, ctypes.byref(mode))
        mode.value &= ~0x0040
        ctypes.windll.kernel32.SetConsoleMode(self.ctypes_handle, mode)
