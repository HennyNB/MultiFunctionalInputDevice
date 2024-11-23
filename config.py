import os
import time


class Config(object):
    root_path = '.\\'

    doc_path = root_path + '_doc_\\'
    log_path = root_path + '_log_\\'
    var_path = root_path + '_data_\\'

    each_line_writer_path = var_path + 'each_line_writer\\'
    information_typewriter_path = var_path + 'information_typewriter\\'
    same_information_writer_path = var_path + 'same_information_writer\\'

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

    @staticmethod
    def editor_title():
        print('========================================')
        print('             多功能输入装置')
        print('            制作：Henny-發龘')
        print('             QQ：2669753313')
        print('           原创不易，侵权必究')
        print('========================================')

    def function_title(self, flag):
        print('')
        self.editor_title()
        print(f'             {str(flag)}')
        self.tips()

    @staticmethod
    def choices_title():
        print('           [0]： 退出输入程序')
        print('           [1]： 信息自动输入')
        print('           [2]： 逐行读取输入')
        print('           [3]： 重复信息输入')
        print('           [4]： 获取项目源码')
        print('========================================')

    @staticmethod
    def be_exiting():
        print('                正在退出')

    @staticmethod
    def have_exited():
        print('                 已退出')

    @staticmethod
    def be_getting():
        print('                 获取中')

    @staticmethod
    def have_gotten():
        print('                下载成功')

    @staticmethod
    def download_error():
        print('    【错误】下载失败，请检查网络连接')

    @staticmethod
    def input_error():
        os.system('cls')
        print('       【错误】输入有误，再次输入')

    @staticmethod
    def try_installing_modules(module):
        print(f'尝试安装模块：{module}')

    @staticmethod
    def tips():
        print('========================================')
        print('          请将光标移动至对话框')
        print('')
        print('           并将发送快捷键改成')
        print('              Ctrl + Enter')

    def waiting_to_writing(self):
        print('')

        for i in range(3):
            print('           距离输入还有 0%d 秒' % (3 - i) + '\r', end='')
            time.sleep(1)

        os.system('cls')
        print('')
        self.editor_title()

    def end(self):
        time.sleep(1)
        os.system('cls')

        print('')
        self.editor_title()

        print('          信息输入已经顺利完成')
        print('========================================')
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

        print('              正在结束进程')
        print('========================================')
        print('')

        print('')
        self.be_exiting()

        print('')
        time.sleep(2)

        self.have_exited()
        time.sleep(1)
