#!/usr/bin/python
# -*-coding: utf-8 -*-

#2. Contar cuántos perros y gatos hay.

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)



perros=0
for r in doc["result"]:
	if r["especie"]=="Canina":
		perros=perros+1
print "Hay ",perros," perros."

gatos=0
for r in doc["result"]:
	if r["especie"]=="Felina":
		gatos=gatos+1
print "Hay ",gatos," gatos"