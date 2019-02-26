import psutil
import time
import sys
import configparser
import datetime
import json


class Monitor:
    def __init__(self):
        self.snap_num = 0
        conf = Monitor_config_parser.parse_config()
        self.out_format = conf['outputformat']
        self.interval = conf['sleepinterval']
        self.output_path = conf['outputpath']

    def run(self):
        self.__output(self.__take_snapshot())
        while(True):
            time.sleep(int(self.interval))
            self.__output(self.__take_snapshot())

    def __take_snapshot(self):
        snapshot = {}
        snapshot['cpu'] = psutil.cpu_percent(interval=0.1)
        data = psutil.disk_usage('/')
        snapshot['memory'] = {'total': data.total, 'used': data.used, 'percent': data.percent}
        data = psutil.virtual_memory()
        snapshot['virtual_memory'] = {'total': data.total, 'used': data.used}
        snapshot['virtual_memory']['percent'] = data.percent
        data = psutil.disk_io_counters(perdisk=False)
        snapshot['io_info'] = {'write_count': data.write_count, 'read_count': data.read_count}
        data = psutil.net_if_stats()
        for i in data.keys():
            data[i] = {'isup': data[i].isup, 'speed': data[i].speed, 'mtu': data[i].mtu}
        snapshot['network_info'] = data
        self.timestamp = str(datetime.datetime.now())
        self.snap_num += 1
        return snapshot

    def __output(self, snapshot):
        if self.out_format == 'text':
            self.__output_text(snapshot)
        elif self.out_format == 'json':
            self.__output_json(snapshot)

    def __output_text(self, snapshot):
        with open(self.output_path, 'a+') as out:
            out.write('SNAPSHOT {}: TIMESTAMP {}: '.format(self.snap_num, self.timestamp))
            out.write('%s \n' % str(snapshot))

    def __output_json(self, snapshot):
        snapshot = {'snapshot': self.snap_num, 'timestamp': self.timestamp, 'data': snapshot}
        with open(self.output_path, 'a+') as out:
            json.dump(snapshot, out, indent=4)


class Monitor_config_parser:

    @staticmethod
    def parse_config():
        config = configparser.ConfigParser()
        config.read('monitor.ini')
        if not Monitor_config_parser.__check_config(config):
            sys.exit()
        return dict(config['common'])

    @staticmethod
    def __check_config(config):
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
