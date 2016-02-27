#!/usr/bin/python
# -*-coding: utf-8 -*-

#4. Pedir por teclado el tamaño del animal y mostrar una lista con la edad y la raza.

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)

cadena=raw_input("Introduce el tamaño del animal: ")
for t in doc["result"]:
	if t.get("tamagno", 0):
		if t["tamagno"].startswith(cadena):
			print "La edad es ",t["edad"],"y la raza es ",t["raza"]