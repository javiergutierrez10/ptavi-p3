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
        
        self.datalist = []
        
    def startElement(self, name, attrs):

        if name == 'root_layout':
            self.datalist.append('root_layout')
            
            self.width = attrs.get('width', "")
            if self.width != " ":
                self.datalist.append(self.width)
            self.height = attrs.get('heigth', "")
            
            if self.height != " ":
                self.datalist.append(self.height)
                
            self.background_color = attrs.get('background_color', "")
            if self.background_color != " ":
                self.datalist.append(self.background-color)
                
        elif name == 'region':
            self.datalist.append('region')
            
            
            self.id = attrs.get('id', "")
            if self.id != " ":
                self.datalist.append(self.id)
                
            self.top = attrs.get('top', "")
            if self.top != " ":
                self.datalist.append(self.top)
            
            self.bottom = attrs.get('bottom', "")
            if self.bottom != " ":
                self.datalist.append(self.bottom)
            
            self.left = attrs.get('left', "")
            if self.left != " ":
                self.datalist.append(self.left)
            
            self.right = attrs.get('right', "")
            if self.right != " ":
                self.datalist.append(self.right)
            
        elif name == 'img':
            self.datalist.append('img')
            
            self.src = attrs.get('src', "")
            if self.src != " ":
                self.datalist.append(self.src)
            
            self.region = attrs.get('region', "")
            if self.region != " ":
                self.datalist.append(self.region)
           
            self.begin = attrs.get('begin', "")
            if self.begin != " ":
                self.datalist.append(self.begin)
            
            self.dur = attrs.get('dur', "")
            if self.dur != " ":
                self.datalist.append(self.dur)
                
        elif name == 'audio':
            self.datalist.append('audio')
            
            self.src = attrs.get('src', "")
            if self.src != " ":
                self.datalist.append(self.src)
            self.begin = attrs.get('begin', "")
            if self.begin != " ":
                self.datalist.append(self.begin)
            
            self.dur = attrs.get('dur', "")
            if self.dur != " ":  
                self.datalist.append(self.dur)
            
        elif name == 'textstream':
            self.datalist.append('textstream')
            
            self.src = attrs.get('src', "")
            if self.src != " ":    
                self.datalist.append(self.src)
            
            self.region = attrs.get('region', "")
            if self.region != " ":
                self.datalist.append(self.region)
            
if __name__ == "__main__":

    parser = make_parser() #Salto línea a línea
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler) #ligar el parser con el manejador
    parser.parse(open('karaoke.smil')) #parseame el archivo
    print(cHandler.datalist)

