import os
import sys

sys.path.append('.\\')
import config


class Creator(object):

    def __init__(self):
        self.config = config.Config()

    def path_creator(self):
        [os.mkdir(i) for i in self.config.path_list if not os.path.exists(i)]

    def file_creator(self):
        for file in self.config.file_list:
            if not os.path.exists(file):
                with open(file=file, mode='w', encoding='UTF-8'):
                    pass

    def file_filler(self):
        for files in self.config.file_list:
            if files == self.config.same_information_writer_quantity_path:
                if open(file=files, mode='r', encoding='UTF-8').read() == '':
                    with open(file=files, mode='w', encoding='UTF-8') as file:
                        file.write('0')

    def total_creator(self):
        self.path_creator()
        self.file_creator()
        self.file_filler()
