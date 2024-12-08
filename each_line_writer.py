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

    def each_line_writer(self):
        os.system('cls')
        self.config.function_title(flag='逐行读取轰炸器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.each_line_writer_text_path, mode='r', encoding='UTF-8') as file:
            lines = file.readlines()

        total_times = len(lines)

        print('')

        for item in range(total_times):
            self.progress_bar.progress_bar(item=item, total=total_times)

            line = lines[item]

            pyperclip.copy(line)
            pyautogui.hotkey('Ctrl', 'V')
            pyautogui.hotkey('Ctrl', 'Enter')

        self.config.end()
