import os
import sys
import time
import pyautogui
import pyperclip

sys.path.append('.\\')
import config
import progress_bar


class EachLineWriter(object):
    config = config.Config()
    progress_bar = progress_bar.ProgressBar()

    title = '逐行读取轰炸器'

    def each_line_writer(self):
        os.system('cls')
        self.config.function_title(flag=self.title)

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.textdata_path, mode='r', encoding='UTF-8') as file:
            lines = file.readlines()

        total_times = len(lines)
        pyautogui.keyDown('Ctrl')
        self.config.text_middle()

        for item in range(total_times):
            self.progress_bar.progress_bar(item=item, total=total_times)
            line = lines[item]

            pyperclip.copy(line)
            pyautogui.press('V')
            pyautogui.press('Enter')

        pyautogui.keyUp('Ctrl')
        self.config.end()
