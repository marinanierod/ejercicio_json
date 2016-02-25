#!/usr/bin/python
# -*-coding: utf-8 -*-

#1. Listar todos los identificadores de los perros junto a sus razas.

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)

for r in doc["result"]:
	print "El identificador es ",r["id"]," y su raza es ",r["raza"]