import os
import sys
import time
import pynput
import string
import pyperclip

sys.path.append('.\\')
import config
import progress_bar


class InformationTypewriter(object):
    config = config.Config()
    progress_bar = progress_bar.ProgressBar()

    keyboard = pynput.keyboard.Controller()

    string_list = (string.punctuation + '·1234567890-=【】；’、，。、~！@#￥%……&*（）——+{}：“|《》？' +
                   'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' + ' \n')

    def information_typewriter(self):
        os.system('cls')
        self.config.function_title(flag='信息自动输入器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.textdata_path, mode='r', encoding='UTF-8') as file:
            content = file.read()

        with open(file=self.config.interval_path, mode='r', encoding='UTF-8') as file:
            quantity = file.read()

        interval = float(quantity)
        total_times = len(content)
        print('')

        for it in range(total_times):
            self.progress_bar.progress_bar(total=total_times, item=it)
            item = content[it]

            for char in item:
                if (char in self.string_list) or ('\u4e00' <= char <= '\u9fff'):
                    self.keyboard.type(char)
                    time.sleep(interval)

                else:
                    pyperclip.copy(char)
                    self.keyboard.press(key='Ctrl')
                    self.keyboard.pressed()

        self.config.end()
