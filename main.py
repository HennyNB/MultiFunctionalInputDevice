import sys

sys.path.append('.\\')


class MainProgramme(object):

    def __init__(self):
        self.creator = None
        self.control = None
        self.manager = None
        self.important_information_writer = None

    def operator(self):
        import control

        self.control = control.Control()
        self.control.control()

    def total_creator(self):
        import creator

        self.creator = creator.Creator()
        self.creator.total_creator()

    def information_writer(self):
        import important_information_writer

        self.important_information_writer = important_information_writer.ImportantInformationWriter()
        self.important_information_writer.writer()

    def main(self):
        import manager

        self.manager = manager.Manager()
        self.manager.manager()


def main():
    main_programme = MainProgramme()

    main_programme.total_creator()
    main_programme.operator()
    main_programme.information_writer()
    main_programme.main()


if __name__ == '__main__':
    main()
