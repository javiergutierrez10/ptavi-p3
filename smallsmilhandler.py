#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.datalist = []
        self.tags = {'root-layout': {'width', 'height', 'background-color'},
                     'region': {'id', 'top', 'bottom', 'left', 'right'},
                     'img': {'src', 'region', 'begin', 'dur'},
                     'audio': {'src', 'begin', 'dur'},
                     'textstream': {'src', 'region'}}

    def startElement(self, name, attrs):

        tmp_list = []
        if name in self.tags:
            self.datalist.append(name)
            for values in self.tags[name]:
                tmp_list.append(values)
                value = attrs.get(values, "")
                if value != "":
                    tmp_list.append(value)
            self.datalist.append(tmp_list)

    def get_tags(self):
        return self.datalist

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
