import sys
import decimal

sys.path.append('.\\')
import config


class ProgressBar(object):
    config = config.Config()

    filled_text = '='
    unfilled_text = '-'

    progress_title = '当前进度：'

    identifiable_sting_list = []
    unidentifiable_sting_list = []

    for word in progress_title:
        if word not in config.string_list:
            unidentifiable_sting_list.append(word)

        if word in config.string_list:
            identifiable_sting_list.append(word)

    identifiable_sting_quantity = len(identifiable_sting_list) * 1
    unidentifiable_string_quantity = len(unidentifiable_sting_list) * 2

    len_title = identifiable_sting_quantity + unidentifiable_string_quantity
    len_config = 10

    decimal_places = 2
    bar_end_space_quantity = 1

    bar_length = config.split_quantity - len_title - len_config - decimal_places - bar_end_space_quantity

    @staticmethod
    def rounder(number: float, n: int):
        num = decimal.Decimal(number)
        side = str('0.' + '0' * n)
        round_config = decimal.Decimal(side)
        rounded = num.quantize(round_config)

        return rounded

    def progress_bar(self, total: int, item: int):
        percents_list = []

        completed_length = int(self.bar_length * item / total)
        uncompleted_length = self.bar_length - completed_length

        percents = self.rounder(100 * item / total, self.decimal_places)
        [percents_list.append(quantities) for quantities in str(percents)]

        bar = self.filled_text * completed_length + self.unfilled_text * uncompleted_length

        def output_config(filled: str, percent_bar: str):
            out_put = ('\r' + self.progress_title + '[' + filled + '] ' +
                       percent_bar + ' %' + ' ' * self.bar_end_space_quantity)

            print(out_put, end='')

        def output(percent_bar: str, flag: str):
            if flag == 'programme':
                output_config(filled=bar, percent_bar=percent_bar)

            elif flag == 'end':
                output_config(filled=self.filled_text * self.bar_length, percent_bar=percent_bar)

        def programme(percent: str):
            if item + 1 == total:
                output(percent_bar='100.' + '0' * self.decimal_places, flag='end')

            elif item + 1 < total:
                output(percent_bar=percent, flag='programme')

        percent_list = ['0' * (4 + self.decimal_places - len(percents_list))] + percents_list
        programme(percent=str(''.join(percent_list)))
