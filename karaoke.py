#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
    
    try:
        filesmil = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    
    parser = make_parser() #Salto línea a línea
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler) #ligar el parser con el manejador
    parser.parse(open(filesmil)) #parseame el archivo
    data = cHandler.get_tags()
    
    
