from urllib.request import *
from lxml.etree import *


class UpdateChecker(object):

    def __init__(self):
        getMessage = self.getMessage
        getVersion = self.getVersion

    def getVersion(self, currentTag):
        url = self.URL
        update = urlopen(url).read()
        root = XML(update)
        cur_version = root.find(".//"+currentTag)
        current = cur_version.text
        return current

    def getMessage(self, messageTag):
        url = self.URL
        update = urlopen(url).read()
        root = XML(update)
        mess = root.find(".//"+messageTag)
        message = mess.text
        return message
