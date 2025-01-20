import os
import time
import datetime


class Config(object):
    root_path = '.\\'

    internal_path = root_path + '_internal' + '\\'

    doc_path = internal_path + '_docs_' + '\\'
    log_path = internal_path + '_logs_' + '\\'
    data_path = internal_path + '_datas_' + '\\'

    information_path = doc_path + 'information.txt'
    requirements_path = doc_path + 'requirements.txt'

    logs_path = log_path + 'event.log'

    textdata_path = data_path + 'text.txt'
    interval_path = data_path + 'interval.txt'
    times_path = data_path + 'times.txt'

    path_list = [root_path, internal_path, doc_path, log_path, data_path]
    file_list = [information_path, requirements_path, logs_path, textdata_path, interval_path, times_path]

    next = '\n'

    split_quantity = 50

    weight = split_quantity
    height = 15

    split_text = '='

    old_title = 'Python-3.12.8'
    new_title = '多功能输入装置'

    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def setting_configs(self):
        os.system('title ' + self.old_title)
        os.system('color 0F')
        os.system('mode con cols=' + str(self.weight) + ' lines=' + str(self.height))

    def split(self):
        content = self.split_text * self.split_quantity
        print(content)

    def calculator(self, number: str):
        num = [j for i in number for j in i if j in self.number_list]

        if num[0] == '0' and '.' in num and len(num) > 1:
            num.remove(num[0])

        splot = ''.join(num)
        return splot

    @staticmethod
    def text_length(text: str):
        length = len(text)
        utf_8_length = len(text.encode('UTF-8'))

        string_length = utf_8_length / 2 - length / 2 + length
        return int(string_length)

    def text_middle(self, text: str = '', end: str = ''):
        string_length = self.text_length(text=text)
        double = self.split_quantity - string_length

        front_space_quantity_float = double / 2
        front_space_quantity = int(front_space_quantity_float)
        front_space = ' ' * front_space_quantity

        end_space_quantity = self.split_quantity - front_space_quantity - self.text_length(text=text)
        end_space = ' ' * end_space_quantity

        string = front_space + text + end_space

        if end == '\r':
            print(end + string, end='')

        else:
            print(string)

    def author_title(self):
        self.split()
        self.text_middle(text=self.new_title)
        self.text_middle(text='作者：Henny-發龘')
        self.text_middle(text='QQ：2669753313')
        self.text_middle(text='版权所有，盗版必究')
        self.split()

    def function_title(self, flag: str):
        self.text_middle()
        self.author_title()
        self.text_middle(text=flag)
        self.tips()

    def choices_title(self):
        self.text_middle(text='[0]： 退出输入程序')
        self.text_middle(text='[1]： 信息自动输入')
        self.text_middle(text='[2]： 逐行读取输入')
        self.text_middle(text='[3]： 重复信息输入')
        self.text_middle(text='[4]： 立即输入数据')
        self.split()

    def be_exiting(self):
        self.text_middle(text='正在退出')

    def have_exited(self):
        self.text_middle(text='已退出')

    def input_error(self):
        os.system('cls')
        self.text_middle(text='【错误】输入有误，再次输入')

    def data_inputer_tips(self):
        os.system('cls')
        self.text_middle(text='请输入数据')

    def tips(self):
        self.split()
        self.text_middle(text='请将对话框发送快捷键改成')
        self.text_middle(text='Ctrl + Enter')
        self.text_middle(text='并切换英文输入法')

    def waiting_to_writing(self):
        self.text_middle()

        for item in range(3):
            self.text_middle(text='距离输入还有 0' + str(3 - item) + ' 秒', end='\r')
            time.sleep(1)

        os.system('cls')
        self.text_middle()
        self.author_title()

    def end(self):
        time.sleep(1)
        os.system('cls')

        self.text_middle()
        self.author_title()

        self.text_middle(text='信息输入已经顺利完成')
        self.split()
        self.text_middle()

        self.text_middle()
        self.be_exiting()

        self.text_middle()
        time.sleep(2)

        self.have_exited()
        time.sleep(1)

    def close_programme(self):
        os.system('cls')

        self.text_middle()
        self.author_title()

        self.text_middle(text='正在结束进程')
        self.split()
        self.text_middle()

        self.text_middle()
        self.be_exiting()

        self.text_middle()
        time.sleep(2)

        self.have_exited()
        time.sleep(1)

    @staticmethod
    def now():
        now = str(datetime.datetime.now())
        now_list = now.split('.')

        return now_list[0]
