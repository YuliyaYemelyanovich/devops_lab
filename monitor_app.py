import psutil
import time
import sys
import configparser

class Monitor:
	def __init__(self):
		self.snap_num = 0
		conf = Monitor_config_parser.parse_config()
		self.conf_format = conf['outputformat']
		self.interval = conf['sleepinterval']
		self.output_path = conf['outputpath']

	def __take_snapshot(self):
		snapshot = {}
		snapshot['cpu'] = psutil.cpu_percent(interval=0.1)
		snapshot['memory'] = psutil.disk_usage('/')
		snapshot['virtual_memory'] = psutil.virtual_memory()
		snapshot['io_info'] = psutil.disk_io_counters(perdisk=False)
		snapshot['network_info'] = psutil.net_if_stats()
		self.snap_num += 1
		return snapshot

	def run(self):
		Monitor_output.output(self.conf_format, self.__take_snapshot())
		'''while(True):
			time.sleep(self.interval)
			Monitor_output.output(self.conf_format, self.__take_snapshot())'''

class Monitor_output:

	def output(format, snapshot):
		if format == 'text':
			Monitor_output.__output_text(snapshot)
		elif format == 'json':
			Monitor_output.__output_json(snapshot)
		else:
			print('invalid config file')

	def __output_text(snapshot):
		print('text')
		print(snapshot)

	def __output_json(snapshot):
		print('json')
		print(snapshot)

class Monitor_config_parser:

	@staticmethod
	def parse_config():
		config = configparser.ConfigParser()
		config.read('monitor.ini')
		if not Monitor_config_parser.check_config(config):
			sys.exit()
		return dict(config['common'])

	@staticmethod
	def check_config(config):
		if 'common' not in config:
			print('Error while parsing config file! No section common found!')
			return False
		elif 'sleepinterval' not in config['common']:
			print('Error while parsing config file! No parameter SleepInterval found!')
			return False
		elif 'outputformat' not in config['common']:
			print('Error while parsing config file! No parameter OutputFormat found!')
			return False
		elif 'outputpath' not in config['common']:
			print('Error while parsing config file! No parameter OutputPath found!')
			return False
		else:
			return True


if __name__ == '__main__':
	monitor = Monitor()
	monitor.run()
