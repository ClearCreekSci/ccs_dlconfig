import os

TAG_USE_METRIC = 'use_metric'
TAG_FREQUENCY = 'frequency'
TAG_PACKAGE_RATE = 'package_rate'
TAG_VERSION = 'version'
TAG_SECRET = 'secret'
TAG_PASSWORD = 'password'

CONFIG_PATH = '/opt/ccs/WeatherDataLogger/settings.cfg'

DEFAULT_VERSION = 1
DEFAULT_METRIC = True
DEFAULT_FREQUENCY = 30
DEFAULT_PACKAGE_RATE = 48
DEFAULT_SECRET = 'deadbeef'
DEFAULT_PASSWORD = ''


class Settings(object):
    
    def __init__(self,path,raise_exceptions=False):
        self.path = path
        self.version = DEFAULT_VERSION
        self.use_metric = DEFAULT_METRIC
        self.frequency = DEFAULT_FREQUENCY
        self.package_rate = DEFAULT_PACKAGE_RATE
        self.secret = DEFAULT_SECRET
        self.passwd = DEFAULT_PASSWORD
        self.raise_exceptions = raise_exceptions
        self.read()

    def read(self):
        if os.path.exists(self.path):
            with open(self.path,'rt') as fd:
                for line in fd:
                    if len(line) > 0:
                        parts = line.split('=')
                        if len(parts) == 2:
                            if parts[0] == TAG_USE_METRIC:
                                if parts[1].strip() == "True":
                                    self.use_metric = True
                                else:
                                    self.use_metric = False
                            elif parts[0].strip() == TAG_FREQUENCY:
                                    self.frequency = int(parts[1].strip())
                            elif parts[0].strip() == TAG_PACKAGE_RATE:
                                    self.package_rate = int(parts[1].strip())
                            elif parts[0].strip() == TAG_VERSION:
                                    self.version = parts[1].strip()
                            elif parts[0].strip() == TAG_SECRET:
                                    self.secret = parts[1].strip()
                            elif parts[0].strip() == TAG_PASSWORD:
                                    self.password = parts[1].strip()
        else:
            if self.raise_exceptions:
                raise FileNotFoundError("Couldn't find file: " + self.path)
            else:
                self.write()

    def write(self):
        with open(self.path,'wt') as fd:
            fd.write(TAG_VERSION + '=' + str(self.version) + '\n')
            fd.write(TAG_USE_METRIC + '=' + str(self.use_metric) + '\n')
            fd.write(TAG_FREQUENCY + '=' + str(self.frequency) + '\n')
            fd.write(TAG_PACKAGE_RATE + '=' + str(self.package_rate) + '\n')
            fd.write(TAG_SECRET + '=' + str(self.secret) + '\n')
            fd.write(TAG_PASSWORD + '=' + str(self.passwd) + '\n')

    def __repr__(self):
        s = TAG_VERSION + ' = ' + str(self.version) + '\n'
        s += TAG_USE_METRIC + ' = ' + str(self.use_metric) + '\n'
        s += TAG_FREQUENCY + ' = ' + str(self.frequency) + '\n'
        s += TAG_PACKAGE_RATE + ' = ' + str(self.package_rate) + '\n'
        s += TAG_SECRET + ' = ' + str(self.secret) + '\n'
        s += TAG_PASSWORD + ' = ' + str(self.passwd) + '\n'
        return s
