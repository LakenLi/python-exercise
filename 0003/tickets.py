#coding:utf-8
#

"""命令行火车票查看器
Usage:
	tickets [-gdtkz] <from> <to> <date>
"""

from docopt import docopt
from stations import stations
import requests
from prettytable import PrettyTable
from colorama import init,Fore
import json



init()

class TrainCollection:
	header = '车次  车站  时间  历时  一等  二等  高级软卧  软卧  硬卧  硬座  无座'.split()

	def __init__(self, available_trains, available_place, options):
		"""查询的火车班次集合
		：param available_trains:一个列表，包含获得的火车班次，每个火车班次是个字典
		；param options:查询的选项
		"""

		self.available_trains = available_trains
		self.available_place = available_place
		self.options = options

	def trains(self):
		for raw_train in self.available_trains:
			raw_train_list = raw_train.split('|')
			train_no = raw_train_list[3]
			initial = train_no[0].lower()
			duration = raw_train_list[10]

			if not self.options or initial in self.options:
				train = [
					train_no,
					'\n'.join([Fore.LIGHTGREEN_EX + self.available_place[raw_train_list[6]] + Fore.RESET,
						Fore.LIGHTRED_EX + self.available_place[raw_train_list[7]] + Fore.RESET]),
					'\n'.join([Fore.LIGHTGREEN_EX + raw_train_list[8] + Fore.RESET,
						Fore.LIGHTRED_EX + raw_train_list[9] + Fore.RESET]),
					duration,
					raw_train_list[-6] if raw_train_list[-6] else '--',
					raw_train_list[-7] if raw_train_list[-7] else '--',
					raw_train_list[-15] if raw_train_list[-15] else '--',
					raw_train_list[-8] if raw_train_list[-8] else '--',
					raw_train_list[-14] if raw_train_list[-14] else '--',
					raw_train_list[-11] if raw_train_list[-11] else '--',
					raw_train_list[-9] if raw_train_list[-9] else '--',
				]
				yield train

	def pretty_print(self):
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains():
			pt.add_row(train)
		print(pt)


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']

    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
                date, from_station, to_station
           )
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url, verify=False)

    available_trains = r.json()['data']['result']
    available_place = r.json()['data']['map']
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    print(arguments)
    TrainCollection(available_trains,available_place, options).pretty_print()


if __name__ == '__main__':
    cli()