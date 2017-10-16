#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler
import json

if __name__ == "__main__":

    try:
        filesmil = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(filesmil))
    data = cHandler.get_tags()

    linea = "\n"
    j = 1
    par = 0
    impar = 1
    while j < (len(data)/2):
        linea = linea + data[par] + "\t"
        i = 1
        while i < len(data[impar]):
            tmp_linea = ""
            tmp_linea = data[impar][i-1] + '="' + data[impar][i] + '"' + "\t"
            i = i + 2
            linea = linea + tmp_linea
        linea = linea + "\n"
        j = j + 1
        par = par + 2
        impar = impar + 2
    print(linea)

    namefile = sys.argv[1].split('.')
    namefile = namefile[0] + '.json'
    with open(namefile, 'w') as file:
        json.dump(linea, file)
