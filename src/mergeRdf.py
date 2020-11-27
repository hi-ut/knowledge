import sys
import bs4
import hashlib
import json
import bs4
import requests
import time
import os
import urllib.parse
import csv
import glob
from rdflib import URIRef, BNode, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from rdflib import Namespace

files = glob.glob("*/**/*.rdf", recursive=True)

all = Graph()

for file in files:

    g = Graph()
    g.parse(file)

    all += g

all.serialize("all.rdf", format='pretty-xml')