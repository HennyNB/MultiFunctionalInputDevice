import sys
import datetime

sys.path.append('.\\')
import config


class ImportantInformationWriter(object):

    def __init__(self):
        self.config = config.Config()

        self.now = str(datetime.datetime.now())

        self.next = '\n'

        self.project_name = '项目名称：多功能输入装置' + self.next
        self.creation_editor = '创建作者：༺ཌༀ Henny✵發龘 ༀད༻' + self.next
        self.creation_time = '创建时间：2023-9-21 13:25:34' + self.next
        self.project_side = '项目地址：https://github.com/HennyNB/MultiFunctionalInputDevice/' + self.next
        self.contact_information = '联系方式：2669753313@qq.com' + self.next
        self.technical_support = '技术支持：PyCharm' + self.next

        self.used_programme = 'Used programme '

        self.pyautogui = 'PyAutoGUI' + self.next
        self.pyperclip = 'pyperclip' + self.next
        self.pypiwin32 = 'pypiwin32' + self.next
        self.tqdm = 'tqdm' + self.next
        self.win32con = 'win32con' + self.next
        self.win32console = 'win32console' + self.next
        self.win32gui = 'win32gui' + self.next

        self.editor_total = str(self.project_name + self.creation_editor + self.creation_time +
                                self.project_side + self.contact_information + self.technical_support)

        self.modules_total = str(self.pyautogui + self.pyperclip + self.pypiwin32 + self.tqdm +
                                 self.win32con + self.win32console + self.win32gui)

        self.used_programme_total = str(self.used_programme + self.now + self.next + self.next)

        self.total = [[self.config.information_path, self.editor_total],
                      [self.config.requirements_path, self.modules_total]]

    def writer(self):
        for i in self.total:
            with open(file=i[0], mode='r', encoding='UTF-8') as file_1:
                if not file_1.read() == i[1]:
                    with open(file=i[0], mode='w', encoding='UTF-8') as file_2:
                        file_2.write(i[1])

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file_3:
            file_3.write(self.used_programme_total)
