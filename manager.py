import sys

sys.path.append('.\\')
import config
import get_source
import each_line_writer
import information_typewriter
import same_information_writer


class Manager(object):
    config = config.Config()
    get_source = get_source.GetSource()
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

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write(total)

    def title(self):
        self.config.editor_title()
        self.config.choices_title()

    def manager(self):
        print('')

        while True:
            self.title()

            print('请选择：', end='')
            flag = input('')

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
                self.get_source.source_operator()

            elif flag == '' or flag.isspace():
                self.flag_writer(flag='None', judgment=self.false)
                self.config.input_error()

            else:
                self.flag_writer(flag=flag, judgment=self.false)
                self.config.input_error()
