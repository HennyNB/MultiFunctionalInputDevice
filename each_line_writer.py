import os
import sys
import time
import tqdm
import pyautogui
import pyperclip

sys.path.append('.\\')
import config


class EachLineWriter(object):

    def __init__(self):
        self.line = None
        self.lines = None

        self.config = config.Config()

    def each_line_writer(self):
        os.system('cls')
        self.config.function_title(flag='逐行读取轰炸器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.each_line_writer_text_path, mode='r', encoding='UTF-8') as file:
            self.lines = file.readlines()

        for i in tqdm.trange(len(self.lines)):
            self.line = self.lines[i]

            pyperclip.copy(self.line)
            pyautogui.hotkey('Ctrl', 'V')
            pyautogui.hotkey('Ctrl', 'Enter')

        self.config.end()
