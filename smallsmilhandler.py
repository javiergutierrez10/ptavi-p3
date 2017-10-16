#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.datalist = []

    def startElement(self, name, attrs):
        tags = {'root-layout': {'width','height','background-color'}, 
                'region': {'id','top','bottom','left','right'},
                'img': {'src','region','begin','dur'},
                'audio': {'src','begin','dur'},
                'textstream': {'src','region'}}

        if name in tags:
            self.datalist.append(name)
            for values in tags[name]:
                self.datalist.append(values)
                value = attrs.get(values, "")
                if value != "":
                    self.datalist.append(value)

        def get_tags(self):
            return self.datalist

if __name__ == "__main__":

    parser = make_parser() #Salto línea a línea
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler) #ligar el parser con el manejador
    parser.parse(open('karaoke.smil')) #parseame el archivo
    print(cHandler.datalist)

