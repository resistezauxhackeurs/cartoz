#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import simplejson
from IPy import IP
from glob import glob
from collections import OrderedDict
from datetime import datetime
import functions_parsing
##from bson import json_util
from lxml import etree
from xml.dom.minidom import parse
from xml.etree import ElementTree
from time     import sleep
import functions_conf
import functions_domains_enum
from fonctions.audit.carto import functions_domains_enum


def scan_domaines(domaine,fichier_domaine):
    """
    Args:
     domaine:
    """
    print ("scan des domaines du projet "+domaine)
    print("domaine analyse " + domaine)
    
    if fichier_domaine == "" : fichier_domaine = "audits/" + domaine + "/domaines_" + domaine + ".txt"
    if not os.path.exists(fichier_domaine):
        functions_domains_enum.audit_domains(domaine, fichier_domaine)

def scan_projets(file_projet):
    #date_audit = time.strftime("%m-%Y")
    with open(file_projet,'r') as f:
        for line in f:
            projet = line.rstrip('\n\r')
            print ("projet analyse " + projet)
            if not os.path.exists("audits/"+projet):os.mkdir("audits/"+projet)
            fichier_domaine = "audits/"+projet+"/domaines_"+projet+".txt"
            if not os.path.exists(fichier_domaine):
                functions_domains_enum.audit_domains(projet,fichier_domaine)