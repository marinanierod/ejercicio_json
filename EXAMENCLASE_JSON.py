#!/usr/bin/python
# -*-coding: utf-8 -*-

import json
with open("ANIMALES_RESCATE.json") as fichero:
	doc=json.load(fichero)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

f=open("index.html","w") 

for r in doc["result"]:
	if r["especie"]=="Canina":
		f.write("<h1>"+str(r.get("nombre", 0))+"</h1>"+"\n")
		f.write("<p>"+str(r.get("raza", 0))+"</p>"+"\n")
		f.write('<img src="http:'+r["foto"]+'"/>'+"\n")
		f.write("\n")

f.close()