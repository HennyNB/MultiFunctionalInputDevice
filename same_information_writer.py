import os
import sys
import time
import pyautogui
import pyperclip

sys.path.append('.\\')
import config
import progress_bar


class SameInformationWriter(object):
    config = config.Config()
    progress_bar = progress_bar.ProgressBar()

    def same_information_writer(self):
        os.system('cls')
        self.config.function_title(flag='重复信息轰炸器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.textdata_path, mode='r', encoding='UTF-8') as file:
            txt = file.read()

        with open(file=self.config.times_path, mode='r', encoding='UTF-8') as file:
            quantity = file.read()

        total_times = int(self.config.calculator(number=quantity))

        pyperclip.copy(txt)
        pyautogui.keyDown('Ctrl')
        print('')

        for item in range(total_times):
            self.progress_bar.progress_bar(total=total_times, item=item)

            pyautogui.press('V')
            pyautogui.press('Enter')

        pyautogui.keyUp('Ctrl')
        self.config.end()
