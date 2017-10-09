#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser #De este sitio importame esta variable
from xml.sax.handler import ContentHandler #Manejador genérico (Le decimos que hacer cuando se encuentre cosas específicas)

class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = False
        self.respuesta = ""
        self.inRespuesta = False
        self.variable = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'chiste':
            # De esta manera tomamos los valores de los atributos
            self.calificacion = attrs.get('calificacion', "")
            self.variable.append(self.calificacion)
        elif name == 'pregunta':
            self.inPregunta = True
        elif name == 'respuesta':
            self.inRespuesta = True

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.variable.append(self.pregunta)
            self.pregunta = ""
            self.inPregunta = False
        if name == 'respuesta':
            self.variable.append(self.respuesta)
            self.respuesta = ""
            self.inRespuesta = False

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char #equivalente (concatena)
        if self.inRespuesta:
            self.respuesta += char #equivalente

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser() #Salto línea a línea
    cHandler = ChistesHandler() #Maneja los chistes
    parser.setContentHandler(cHandler) #ligar el parser con el manejador
    parser.parse(open('chistes2.xml')) #parseame el archivo
    print(cHandler.variable)


