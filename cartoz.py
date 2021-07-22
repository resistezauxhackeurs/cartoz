#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Utilisation fuzzing
import sys,re,os
sys.path.append("fonctions")
sys.path.append("fonctions/config")
sys.path.append("fonctions/audit")
sys.path.append("fonctions/audit/carto")
import functions_scan_projet
import functions_conf
import argparse
#copy files
functions_conf.verif_vulneers()



parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domaine", help="Domaine a analyser.", nargs='*')
parser.add_argument("--enum", "--enum", help="Enumerer les domaines", nargs='*')
parser.add_argument("--scan_file_projet", "--scan_file_projet", help="Scan de fichier de projet via fichier texte", nargs='*')
args = parser.parse_args()


fichier_domaine = ""
file_projet = ""

if args.scan_file_projet:
	file_projet=' '.join(args.scan_file_projet)
	if file_projet == "":
		print("entrez le fichier des projets à scanner (fichier txt)")
	else:
		print("scan de projets contenus dans le fichier "+file_projet)
		functions_scan_projet.scan_projets(file_projet)
		exit()


if args.domaine :
	domaine=' '.join(args.domaine)
	print("domaine analyse : " + str(domaine))
	check_domaine = re.match(r'^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,5}$',domaine)
	if check_domaine is None:
		print("Le domaine " + str(domaine) + " est non-valide. Exemple de domaine valide : exemple.fr") 
		exit()
else:
	print("le domaine doit etre indique")
	exit()


if args.enum or args.enum is not None :
	print("cartographie des domaines du projet" + domaine)
	functions_scan_projet.scan_domaines(domaine,"")
	exit()
