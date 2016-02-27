#!/usr/bin/python
# -*-coding: utf-8 -*-

#5. Pedir por teclado el sexo del animal para mostrar  las url de las imágenes y su raza.

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)

cadena=raw_input("Introduce el sexo del animal: ")
for s in doc["result"]:
	if s["sexo"]==cadena:
		print "FOTO: ",s["foto"]," RAZA: ",s["raza"]

