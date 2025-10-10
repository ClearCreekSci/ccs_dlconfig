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

