import os
import time
import datetime


class Config(object):
    root_path = '.\\'

    doc_path = root_path + '_doc_\\'
    log_path = root_path + '_log_\\'
    data_path = root_path + '_data_\\'
    source_path = root_path + '_source_\\'

    zip_file_path = root_path + 'file.zip'
    information_path = doc_path + 'information.txt'
    requirements_path = doc_path + 'requirements.txt'

    logs_path = log_path + 'event.log'

    textdata_path = data_path + 'text.txt'
    interval_path = data_path + 'interval.txt'
    times_path = data_path + 'times.txt'

    path_list = [root_path, doc_path, log_path, data_path]
    file_list = [information_path, requirements_path, logs_path, textdata_path, interval_path, times_path]

    next = '\n'

    split_quantity = 50

    split_text = '='
    window_title = '多功能输入装置'

    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def split(self):
        content = self.split_text * self.split_quantity

        return content

    def times_calculator(self, number: str):
        num = [j for i in number for j in i if j in self.number_list]

        if num[0] == '0' and len(num) > 1:
            num.remove(num[0])

        after = ''.join(num)
        return after

    @staticmethod
    def text_length(text: str):
        length = len(text)
        utf_8_length = len(text.encode('UTF-8'))

        string_length = utf_8_length / 2 - length / 2 + length
        return int(string_length)

    def text_middle(self, text: str):
        string_length = self.text_length(text=text)
        double = self.split_quantity - string_length
        space_quantity_float = double / 2
        space_quantity = int(space_quantity_float)

        string = ' ' * space_quantity + text
        return string

    def editor_title(self):
        print(self.split())
        print(self.text_middle(text='多功能输入装置'))
        print(self.text_middle(text='制作：Henny-發龘'))
        print(self.text_middle(text='QQ：2669753313'))
        print(self.text_middle(text='技术支持：PyCharm'))
        print(self.split())

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
        print(self.split())

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
        print(self.split())
        print(self.text_middle(text='请将对话框发送快捷键改成'))
        print(self.text_middle(text='Ctrl + Enter'))
        print(self.text_middle(text='并切换英文输入法'))

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
        print(self.split())
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
        print(self.split())
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
