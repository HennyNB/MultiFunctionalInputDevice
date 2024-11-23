import os
import sys
import time
import tqdm
import pyautogui
import pyperclip

sys.path.append('.\\')
import config


class SameInformationWriter(object):

    def __init__(self):
        self.txt = None
        self.quantity = None

        self.num = None
        self.number = None

        self.config = config.Config()

        self.string_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def same_information_writer(self):
        os.system('cls')
        self.config.function_title(flag='重复信息轰炸器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.same_information_writer_text_path, mode='r', encoding='UTF-8') as file_1:
            self.txt = file_1.read()

        with open(file=self.config.same_information_writer_quantity_path, mode='r', encoding='UTF-8') as file_2:
            self.quantity = file_2.readlines()

        self.num = [j for i in self.quantity for j in i if j in self.string_list]

        if self.num[0] == '0' and len(self.num) > 1:
            self.num.remove(self.num[0])

        self.number = ''.join(self.num)

        pyperclip.copy(self.txt)

        for _ in tqdm.trange(eval(self.number)):
            pyautogui.hotkey('Ctrl', 'V')
            pyautogui.hotkey('Ctrl', 'Enter')

        pyautogui.write('\n')

        self.config.end()
