import sys

sys.path.append('.\\')
import config
import creator
import data_inputer
import each_line_writer
import information_typewriter
import same_information_writer


class Manager(object):
    config = config.Config()
    creator = creator.Creator()
    data_inputer = data_inputer.DataInputer()
    each_line_writer = each_line_writer.EachLineWriter()
    information_typewriter = information_typewriter.InformationTypewriter()
    same_information_writer = same_information_writer.SameInformationWriter()

    true = 'True'
    false = 'False'
    running = 'Running = '

    space = ' ' * 4

    def flag_writer(self, flag: str, judgment: str):
        choice = 'Flag = ' + str(flag)
        total = str(self.space + self.space + self.config.now() + self.config.next + self.space + self.space +
                    self.space + choice + self.config.next + self.space + self.space + self.space + self.running +
                    judgment + self.config.next + self.config.next)

        self.creator.total_creator()
        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write(total)

    def title(self):
        self.config.author_title()
        self.config.choices_title()

    def manager(self):
        mode = True
        self.config.text_middle()

        while mode:
            self.title()
            flag = input('请选择：')

            if flag == '0':
                self.flag_writer(flag=flag, judgment=self.true)
                self.config.close_programme()

                break

            elif flag == '1':
                self.flag_writer(flag=flag, judgment=self.true)
                self.information_typewriter.information_typewriter()

            elif flag == '2':
                self.flag_writer(flag=flag, judgment=self.true)
                self.each_line_writer.each_line_writer()

            elif flag == '3':
                self.flag_writer(flag=flag, judgment=self.true)
                self.same_information_writer.same_information_writer()

            elif flag == '4':
                self.flag_writer(flag=flag, judgment=self.true)
                self.data_inputer.data_inputer()

            elif flag == '' or flag.isspace():
                self.flag_writer(flag='None', judgment=self.false)
                self.config.input_error()

            else:
                self.flag_writer(flag=flag, judgment=self.false)
                self.config.input_error()
