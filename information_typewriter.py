import os
import sys
import time
import pynput
import pyautogui
import pyperclip

sys.path.append('.\\')
import config
import progress_bar


class InformationTypewriter(object):
    config = config.Config()
    progress_bar = progress_bar.ProgressBar()

    keyboard = pynput.keyboard.Controller()

    title = '信息自动输入器'

    def information_typewriter(self):
        os.system('cls')
        self.config.function_title(flag=self.title)

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.textdata_path, mode='r', encoding='UTF-8') as file:
            content = file.read()

        with open(file=self.config.interval_path, mode='r', encoding='UTF-8') as file:
            quantity = file.read()

        interval = float(quantity)
        total_times = len(content)
        self.config.text_middle()

        for it in range(total_times):
            self.progress_bar.progress_bar(total=total_times, item=it)
            item = content[it]

            for char in item:
                if char.encode('UTF-8'):
                    self.keyboard.type(char)
                    time.sleep(interval)

                else:
                    pyperclip.copy(char)
                    pyautogui.hotkey('Ctrl', 'V')

        self.config.end()
