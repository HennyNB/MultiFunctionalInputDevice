import os
import sys
import time
import tqdm
import pyautogui
import pyperclip

sys.path.append('.\\')
import config


class InformationTypewriter(object):

    def __init__(self):
        self.line = None
        self.lines = None

        self.config = config.Config()

    def information_typewriter(self):
        os.system('cls')
        self.config.function_title(flag='信息自动输入器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.information_typewriter_text_path, mode='r', encoding='UTF-8') as file:
            self.lines = file.readlines()

        for i in tqdm.trange(len(self.lines)):
            self.line = self.lines[i]

            pyperclip.copy(self.line)
            pyautogui.hotkey('Ctrl', 'V')

        self.config.end()
