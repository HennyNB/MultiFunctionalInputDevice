import os
import sys

sys.path.append('.\\')
import config


class Creator(object):
    config = config.Config()

    def path_creator(self):
        [os.mkdir(i) for i in self.config.path_list if not os.path.exists(i)]

    def file_creator(self):
        for file in self.config.file_list:
            if not os.path.exists(file):
                with open(file=file, mode='w', encoding='UTF-8') as each_file:
                    each_file.write('')

    def file_filler(self):
        with open(file=self.config.same_information_writer_quantity_path, mode='r', encoding='UTF-8') as file:
            old = file.read()

        if old == '' or old.isspace():
            with open(file=self.config.same_information_writer_quantity_path, mode='w', encoding='UTF-8') as each_file:
                each_file.write('0')

    def total_creator(self):
        self.path_creator()
        self.file_creator()
        self.file_filler()
