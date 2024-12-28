import sys
import ctypes
import win32con
import win32gui
import pygetwindow

sys.path.append('.\\')
import config


class ConsoleSettings(object):
    config = config.Config()

    @staticmethod
    def find_window(window_title: str, window_class_name: str = 'ConsoleWindowClass'):
        window = win32gui.FindWindow(window_class_name, window_title)
        return window

    def get_old_handle(self):
        handle = self.find_window(window_title='管理员: ' + ' ' + self.config.old_title)
        return handle

    def get_new_handle(self):
        handle = self.find_window(window_title=self.config.new_title)
        return handle

    @staticmethod
    def disable_quickly_edit():
        mode = ctypes.c_ulong()
        window = ctypes.windll.kernel32.GetStdHandle(-10)

        ctypes.windll.kernel32.GetConsoleMode(window, ctypes.byref(mode))
        mode.value &= ~0x0040
        ctypes.windll.kernel32.SetConsoleMode(window, mode)

    def delete_menus(self):
        handle = self.get_new_handle()
        menu = win32gui.GetSystemMenu(handle, 0)

        win32gui.DeleteMenu(menu, win32con.SC_SIZE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(menu, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(menu, win32con.SC_MAXIMIZE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(menu, win32con.SC_MINIMIZE, win32con.MF_BYCOMMAND)

    def set_side(self):
        screen = ctypes.windll.user32.GetSystemMetrics
        window = pygetwindow.getWindowsWithTitle(self.config.new_title)[0]

        screen_x = screen(0)
        screen_y = screen(1)

        window_x = window.width
        window_y = window.height

        side_x = screen_x / 2 - window_x / 2
        side_y = screen_y / 2 - window_y / 2

        x = int(side_x)
        y = int(side_y)

        window.moveTo(x, y)

    def top_most(self):
        handle = self.get_new_handle()
        win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def set_title(self):
        handle = self.get_old_handle()
        win32gui.SetWindowText(handle, self.config.new_title)

    def console_settings(self):
        if self.get_old_handle():
            self.operator()

    def operator(self):
        self.set_title()
        self.top_most()
        self.delete_menus()
        self.set_side()
        self.disable_quickly_edit()
