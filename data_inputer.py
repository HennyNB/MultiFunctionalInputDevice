import os
import sys

sys.path.append('.\\')
import config

class DataInputer(object):
    config = config.Config()

    def data_inputer(self):
        os.system('cls')
        os.system('start ' + self.config.data_path)
        print('')