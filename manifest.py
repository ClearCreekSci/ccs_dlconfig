"""
    manifest.py
    Records data from various sensors

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

"""
import os
import xml.etree.ElementTree as et

TAG_TIME = 'time'
TAG_COMMIT = 'commit'
TAG_VERSION = 'version'

class Manifest(object):

    def __init__(self,raise_exceptions=False):
        self.time = ''
        self.commit = ''
        self.version = ''
        path = os.path.join(os.getcwd(),'manifest.xml')
        self.read(path)

    def read(self,path):
        tree = et.parse(path)
        root = tree.getroot()
        for child in root:
            if child.tag == TAG_TIME:
                self.time = child.text.strip()
            elif child.tag == TAG_COMMIT:
                self.commit = child.text.strip()
            elif child.tag == TAG_VERSION:
                self.version = child.text.strip()

