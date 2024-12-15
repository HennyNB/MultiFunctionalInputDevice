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

    string_list = ('~！@#￥%……&*（）——+{}：“|《》？·-=【】；’、，。' +
                   '~_+{}:"|<>?' + "\n`-=[];'\\',./" + '0123456789'
                   'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')

    def information_typewriter(self):
        os.system('cls')
        self.config.function_title(flag='信息自动输入器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.textdata_path, mode='r', encoding='UTF-8') as file:
            lines = file.readlines()

        with open(file=self.config.interval_path, mode='r', encoding='UTF-8') as file:
            content = file.read()

        interval = float(content)
        total_times = len(lines)
        print('')

        for item in range(total_times):
            self.progress_bar.progress_bar(total=total_times, item=item)
            line = lines[item]

            for char in line:
                if (char in self.string_list) or ('\u4e00' <= char <= '\u9fff'):
                    self.keyboard.type(char)
                    time.sleep(interval)

                else:
                    pyperclip.copy(char)
                    pyautogui.hotkey('Ctrl', 'V')

        self.config.end()
