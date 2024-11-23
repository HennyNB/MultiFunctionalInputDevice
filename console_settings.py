import os
import ctypes
import win32con
import win32gui
import win32console


class ConsoleSettings(object):

    def __init__(self):
        self.menus = None
        self.get_window = None

        self.mode = None
        self.stdin_handle = None

    def console_settings(self):
        self.get_window = win32console.GetConsoleWindow()

        if self.get_window:
            self.settings()

    def settings(self):
        self.menus = win32gui.GetSystemMenu(self.get_window, 0)

        win32gui.DeleteMenu(self.menus, win32con.SC_SIZE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(self.menus, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(self.menus, win32con.SC_MAXIMIZE, win32con.MF_BYCOMMAND)
        win32gui.DeleteMenu(self.menus, win32con.SC_MINIMIZE, win32con.MF_BYCOMMAND)

        os.system('title 多功能输入装置')
        os.system('color 0F')
        os.system('mode con cols=40  lines=15')

        self.enable_quick_edit_mode()

    def enable_quick_edit_mode(self):
        self.stdin_handle = ctypes.windll.kernel32.GetStdHandle(-10)
        self.mode = ctypes.c_ulong()

        ctypes.windll.kernel32.GetConsoleMode(self.stdin_handle, ctypes.byref(self.mode))
        self.mode.value &= ~0x0040
        ctypes.windll.kernel32.SetConsoleMode(self.stdin_handle, self.mode)
