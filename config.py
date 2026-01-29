'''
    config.py
    Configuration for recording data from various sensors

    Copyright (C) 2025 Clear Creek Scientific

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os
import xml.etree.ElementTree as et

TAG_DATA = 'data'
TAG_LOG = 'log'
TAG_PATHS = 'paths'
TAG_ROOT = 'ccs-config'
TAG_VERSION = 'version'

DEFAULT_DATA_DIR = './data'
DEFAULT_LOG_DIR = './log'
DEFAULT_VERSION = '2'

XML_DECL = '<?xml version="1.0" encoding="UTF-8"?>'

'''
TAG_USE_METRIC = 'use_metric'
TAG_FREQUENCY = 'frequency'
TAG_PACKAGE_RATE = 'package_rate'
TAG_VERSION = 'version'
TAG_SECRET = 'secret'
TAG_PASSWORD = 'password'

DEFAULT_VERSION = 1
DEFAULT_METRIC = True
DEFAULT_FREQUENCY = 30
DEFAULT_PACKAGE_RATE = 48
DEFAULT_SECRET = 'deadbeef'
DEFAULT_PASSWORD = ''
'''

class Settings(object):
    
    def __init__(self,path,raise_exceptions=False):
        self.path = path
        self.raise_exceptions = raise_exceptions
        self.data_dir = DEFAULT_DATA_DIR
        self.log_dir = DEFAULT_LOG_DIR
        self.tree = None
        self.root = None
        self.version = None
        #self.version = DEFAULT_VERSION
        #self.use_metric = DEFAULT_METRIC
        #self.frequency = DEFAULT_FREQUENCY
        #self.package_rate = DEFAULT_PACKAGE_RATE
        #self.secret = DEFAULT_SECRET
        #self.passwd = DEFAULT_PASSWORD
        self.read()

    def read(self):
        if os.path.exists(self.path):
            self.tree = et.parse(self.path)
            self.root = tree.getroot()
            self.version = int(self.root.attrib['version'])
            for path in root.findall(TAG_PATHS):
                data = path.find(TAG_DATA)
                if None is not data:
                    self.data_dir = data.text
                else:
                    self.data_dir = None
                log = path.find(TAG_LOG)
                if None is not log:
                    self.log_dir = log.text
                else:
                    self.log_dir = None
        else:
            if self.raise_exceptions:
                raise FileNotFoundError("Couldn't find file: " + self.path)
            else:
                self.write()

    def write(self):
        with open(self.path,'wt') as fd:
            fd.write(XML_DECL + '\n')
            fd.write('<' + TAG_ROOT + TAG_VERSION + '="' + DEFAULT_VERSION + '">\n')
            fd.write('<' + TAG_PATHS + '>\n')
            if None is not self.data_dir:
                fd.write('<' + TAG_DATA + '>' + self.data_dir + '</' + TAG_DATA + '>\n')
            if None is not self.log_dir:
                fd.write('<' + TAG_LOG + '>' + self.data_dir + '</' + TAG_LOG + '>\n')
            #fd.write(TAG_VERSION + '=' + str(self.version) + '\n')
            #fd.write(TAG_USE_METRIC + '=' + str(self.use_metric) + '\n')
            #fd.write(TAG_FREQUENCY + '=' + str(self.frequency) + '\n')
            #fd.write(TAG_PACKAGE_RATE + '=' + str(self.package_rate) + '\n')
            #fd.write(TAG_SECRET + '=' + str(self.secret) + '\n')
            #fd.write(TAG_PASSWORD + '=' + str(self.passwd) + '\n')

    def __repr__(self):
        s = TAG_VERSION + ' = ' + str(self.version) + '\n'
        s += TAG_DATA_DIR + ' = ' + str(self.data_dir) + '\n'
        s += TAG_LOG_DIR + ' = ' + str(self.log_dir) + '\n'
        return s


