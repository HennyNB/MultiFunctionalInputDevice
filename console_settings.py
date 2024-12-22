import os
import sys
import ctypes
import pygetwindow

sys.path.append('.\\')
import config


class ConsoleSettings(object):
    config = config.Config()

    weight = config.split_quantity
    height = 15

    @staticmethod
    def disable_quickly_edit():
        mode = ctypes.c_ulong()
        handle = ctypes.windll.kernel32.GetStdHandle()

        ctypes.windll.kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        mode.value &= ~0x0040
        ctypes.windll.kernel32.SetConsoleMode(handle, mode)

    @staticmethod
    def get_screen_side():
        screen = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]
        return screen

    def get_window_side(self):
        window = pygetwindow.getWindowsWithTitle(self.config.window_title)[0]
        return [window.width, window.height]

    def set_side(self):
        window = pygetwindow.getWindowsWithTitle(self.config.window_title)[0]

        window_x = self.get_window_side()[0]
        window_y = self.get_window_side()[1]

        side_x = self.get_screen_side()[0] / 2 - window_x / 2
        side_y = self.get_screen_side()[1] / 2 - window_y / 2

        x = int(side_x)
        y = int(side_y)

        window.moveTo(x, y)

        # 759 400

    def console_settings(self):
        os.system('color 0F')
        os.system('title ' + self.config.window_title)
        os.system('mode con cols=' + str(self.weight) + ' lines=' + str(self.height))

        self.set_side()
        self.disable_quickly_edit()
