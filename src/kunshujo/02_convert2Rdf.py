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

import geohash2

import json

all = Graph()
all.parse("data/new.json", format="json-ld")
all.serialize(destination="data/new.rdf", format='pretty-xml')
