#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
#   Constructor. Inicializamos las variables

        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        
        self.variable = []
        
    def startElement(self, name, attrs):

        if name == 'root_layout':
            self.variable.append('root_layout')
            
            self.width = attrs.get('width', "")
            self.height = attrs.get('heigth', "")
            self.background_color = attrs.get('background_color', "")
            self.variable.append(self.width)
            self.variable.append(self.height)
            self.variable.append(self.background-color)    
        elif name == 'region':
            self.variable.append('region')
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.variable.append(self.id)
            self.variable.append(self.top)
            self.variable.append(self.bottom)
            self.variable.append(self.left)
            self.variable.append(self.right)             
        elif name == 'img':
            self.variable.append('img')
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.variable.append(self.src)
            self.variable.append(self.region)
            self.variable.append(self.begin)
            self.variable.append(self.dur)     
        elif name == 'audio':
            self.variable.append('audio')
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.variable.append(self.src)
            self.variable.append(self.begin)
            self.variable.append(self.dur) 
        elif name == 'textstream':
            self.variable.append('textstream')
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.variable.append(self.src)
            self.variable.append(self.region)
            
if __name__ == "__main__":

    parser = make_parser() #Salto línea a línea
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler) #ligar el parser con el manejador
    parser.parse(open('karaoke.smil')) #parseame el archivo
    print(cHandler.variable)

