#!/usr/bin/python
# -*-coding: utf-8 -*-

#3. Mostrar nombres que empiecen por una cadena introducida por teclado junto con su fecha de ingreso.

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)

cadena=raw_input("Introduce una cadena: ")
for r in doc["result"]:
	if r["especie"]=="Canina":
		if r.get("nombre", 0):
			if r["nombre"].startswith(cadena):
				print "El nombre es ",r["nombre"],"y su fecha de ingreso ",r["fechaIngreso"]


		#if libro["title"]["__text"].startswith(cadena):
		#print libro["title"]["__text"], libro["year"]
