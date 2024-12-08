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

    string_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def same_information_writer(self):
        os.system('cls')
        self.config.function_title(flag='重复信息轰炸器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.same_information_writer_text_path, mode='r', encoding='UTF-8') as file_1:
            txt = file_1.read()

        with open(file=self.config.same_information_writer_quantity_path, mode='r', encoding='UTF-8') as file_2:
            quantity = file_2.readlines()

        num = [j for i in quantity for j in i if j in self.string_list]

        if num[0] == '0' and len(num) > 1:
            num.remove(num[0])

        number = ''.join(num)
        total_times = eval(number)

        pyperclip.copy(txt)

        print('')
        for item in range(total_times):
            self.progress_bar.progress_bar(total=total_times, item=item)

            pyautogui.hotkey('Ctrl', 'V')
            pyautogui.hotkey('Ctrl', 'Enter')

        self.config.end()
