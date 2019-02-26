import psutil
import time

class Monitor:
	def __init__(self):
		self.snap_num = 0
		self.conf_format = 'text'
		self.interval = 5 * 60
		self.output_path = "./snapshot.log"

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
			__output_text(snapshot)
		elif format == 'json':
			__output_json(snapshot)
		else:
			print('invalid config file')

	def __output_text(snapshot):
		print('text')
		print(snapshot)

	def __output_json(snapshot):
		print('json')
		print(snapshot)

#class Monitor_config_parser:




if __name__ == '__main__':
	monitor = Monitor()
	monitor.run()
