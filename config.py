import os

TAG_USE_METRIC = 'use_metric'
TAG_FREQUENCY = 'frequency'
TAG_PACKAGE_RATE = 'package_rate'

CONFIG_PATH = '/opt/ccs/WeatherLogger/settings.cfg'

DEFAULT_METRIC = True
DEFAULT_FREQUENCY = 30
DEFAULT_PACKAGE_RATE = 48


class Settings(object):
    
    def __init__(self,raise_exceptions=False):
        self.use_metric = DEFAULT_METRIC
        self.frequency = DEFAULT_FREQUENCY
        self.package_rate = DEFAULT_PACKAGE_RATE
        self.read()

    def read(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH,'rt') as fd:
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
        else:
            if raise_exceptions:
                raise FileNotFoundError("Couldn't find file: " + CONFIG_PATH)
            else:
                self.write()

    def write(self):
        with open(CONFIG_PATH,'wt') as fd:
            fd.write(TAG_USE_METRIC + '=' + str(self.use_metric) + '\n')
            fd.write(TAG_FREQUENCY + '=' + str(self.frequency) + '\n')
            fd.write(TAG_PACKAGE_RATE + '=' + str(self.package_rate) + '\n')

