import sys
import datetime

sys.path.append('.\\')
import config
import get_source
import each_line_writer
import information_typewriter
import same_information_writer


class Manager(object):

    def __init__(self):
        self.next = '\n'
        self.space = '    '

        self.true = 'True'
        self.false = 'False'
        self.running = 'Running = '
        self.used_programme = 'Used programme '

        self.now = None
        self.choice = None
        self.total = None

        self.flag = None

        self.config = config.Config()
        self.get_source = get_source.GetSource()
        self.each_line_writer = each_line_writer.EachLineWriter()
        self.information_typewriter = information_typewriter.InformationTypewriter()
        self.same_information_writer = same_information_writer.SameInformationWriter()

    def flag_writer(self, flag, judgment):
        self.now = str(datetime.datetime.now())
        self.choice = 'Flag = ' + str(flag)
        self.total = str(self.space + self.now + self.next + self.space + self.space + self.choice + self.next +
                         self.space + self.space + self.running + judgment + self.next + self.next)

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write(self.total)

    def title(self):
        self.config.editor_title()
        self.config.choices_title()

    def manager(self):
        print('')

        while True:
            self.title()
            self.flag = input('请选择：')

            if self.flag == '0':
                self.flag_writer(flag=self.flag, judgment=self.true)
                self.config.close_programme()
                break

            elif self.flag == '1':
                self.flag_writer(flag=self.flag, judgment=self.true)
                self.information_typewriter.information_typewriter()

            elif self.flag == '2':
                self.flag_writer(flag=self.flag, judgment=self.true)
                self.each_line_writer.each_line_writer()

            elif self.flag == '3':
                self.flag_writer(flag=self.flag, judgment=self.true)
                self.same_information_writer.same_information_writer()

            elif self.flag == '4':
                self.flag_writer(flag=self.flag, judgment=self.true)
                self.get_source.source_operator()

            elif self.flag == '':
                self.flag_writer(flag='None', judgment=self.false)
                self.config.input_error()

            else:
                self.flag_writer(flag=self.flag, judgment=self.false)
                self.config.input_error()
