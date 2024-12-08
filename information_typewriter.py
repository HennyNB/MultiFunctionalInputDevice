import os
import sys
import time
import pyautogui
import pyperclip

sys.path.append('.\\')
import config
import progress_bar


class InformationTypewriter(object):
    config = config.Config()
    progress_bar = progress_bar.ProgressBar()

    def information_typewriter(self):
        os.system('cls')
        self.config.function_title(flag='信息自动输入器')

        time.sleep(2)
        self.config.waiting_to_writing()

        with open(file=self.config.information_typewriter_text_path, mode='r', encoding='UTF-8') as file:
            lines = file.readlines()

        total_times = len(lines)

        print('')
        for item in range(total_times):
            line = lines[item]

            self.progress_bar.progress_bar(total=total_times, item=item)

            pyperclip.copy(line)
            pyautogui.hotkey('Ctrl', 'V')

        self.config.end()
