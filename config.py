import os
import time
import datetime


class Config(object):
    root_path = '.\\'

    doc_path = root_path + '_doc_\\'
    log_path = root_path + '_log_\\'
    var_path = root_path + '_data_\\'
    source_path = root_path + '_source_\\'

    each_line_writer_path = var_path + 'each_line_writer\\'
    information_typewriter_path = var_path + 'information_typewriter\\'
    same_information_writer_path = var_path + 'same_information_writer\\'

    zip_file_path = root_path + 'file.zip'
    information_path = doc_path + 'information.txt'
    requirements_path = doc_path + 'requirements.txt'

    logs_path = log_path + 'event.log'

    information_typewriter_text_path = information_typewriter_path + 'text.txt'

    each_line_writer_text_path = each_line_writer_path + 'text.txt'

    same_information_writer_text_path = same_information_writer_path + 'text.txt'
    same_information_writer_quantity_path = same_information_writer_path + 'quantity.txt'

    path_list = [root_path, doc_path, log_path, var_path,
                 information_typewriter_path, each_line_writer_path,
                 same_information_writer_path]

    file_list = [information_path, requirements_path, logs_path, information_typewriter_text_path,
                 each_line_writer_text_path, same_information_writer_text_path, same_information_writer_quantity_path]

    next = '\n'

    split_quantity = 50

    string_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '█', '?',
                   '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                   '_', '=' '+', '{', '}', '[', ']', ':', ';', '"', "'", '|', '\\',
                   '<', ',', '>', '.', '/']

    filled_text = '='
    unfilled_text = '-'

    progress_title = '输入进度：'

    window_title = '多功能输入装置'

    def text_middle(self, text: str):
        identifiable_sting_list = []
        unidentifiable_sting_list = []

        for item in text:
            if item not in self.string_list:
                unidentifiable_sting_list.append(item)

            if item in self.string_list:
                identifiable_sting_list.append(item)

        identifiable_sting_quantity = len(identifiable_sting_list) * 1
        unidentifiable_string_quantity = len(unidentifiable_sting_list) * 2

        space_quantity = int(
            (self.split_quantity - unidentifiable_string_quantity - identifiable_sting_quantity) / 2)
        text = str(' ' * space_quantity) + str(text)

        return text

    def editor_title(self):
        print('=' * self.split_quantity)
        print(self.text_middle(text='多功能输入装置'))
        print(self.text_middle(text='制作：Henny-發龘'))
        print(self.text_middle(text='QQ：2669753313'))
        print(self.text_middle(text='原创不易，侵权必究'))
        print('=' * self.split_quantity)

    def function_title(self, flag: str):
        print('')
        self.editor_title()
        print(self.text_middle(text=flag))
        self.tips()

    def choices_title(self):
        print(self.text_middle(text='[0]： 退出输入程序'))
        print(self.text_middle(text='[1]： 信息自动输入'))
        print(self.text_middle(text='[2]： 逐行读取输入'))
        print(self.text_middle(text='[3]： 重复信息输入'))
        print(self.text_middle(text='[4]： 获取项目源码'))
        print('=' * self.split_quantity)

    def be_exiting(self):
        print(self.text_middle(text='正在退出'))

    def have_exited(self):
        print(self.text_middle(text='已退出'))

    def be_getting(self):
        print(self.text_middle(text='获取中'))

    def have_gotten(self):
        print(self.text_middle(text='下载成功'))

    def download_error(self):
        print(self.text_middle(text='【错误】下载失败，请检查网络连接'))

    def input_error(self):
        os.system('cls')
        print(self.text_middle(text='【错误】输入有误，再次输入'))

    @staticmethod
    def try_installing_modules(module):
        print('尝试安装模块：' + module)

    def tips(self):
        print('=' * self.split_quantity)
        print(self.text_middle(text='请将光标移动至对话框'))
        print('')
        print(self.text_middle(text='并将发送快捷键改成'))
        print(self.text_middle(text='  Ctrl + Enter'))

    def waiting_to_writing(self):
        print('')

        for item in range(3):
            print(self.text_middle(text='距离输入还有 0' + str(3 - item) + ' 秒') + '\r', end='')
            time.sleep(1)

        os.system('cls')
        print('')
        self.editor_title()

    def end(self):
        time.sleep(1)
        os.system('cls')

        print('')
        self.editor_title()

        print(self.text_middle(text='信息输入已经顺利完成'))
        print('=' * self.split_quantity)
        print('')

        print('')
        self.be_exiting()

        print('')
        time.sleep(2)

        self.have_exited()
        time.sleep(1)

        os.system('cls')
        print('')

    def close_programme(self):
        os.system('cls')

        print('')
        self.editor_title()

        print(self.text_middle(text='正在结束进程'))
        print('=' * self.split_quantity)
        print('')

        print('')
        self.be_exiting()

        print('')
        time.sleep(2)

        self.have_exited()
        time.sleep(1)

    @staticmethod
    def now():
        now = str(datetime.datetime.now())
        now_list = now.split('.')

        return now_list[0]
