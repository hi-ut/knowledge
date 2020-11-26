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



rows = []

rows.append(["Name", "Text", "Pic", "Birth Date", "兄弟", "子", "URL"])


files = glob.glob("../../docs/api/entity/chname/*.json")
for file in files:
    print(file)
    json_open = open(file, 'r')
    json_load = json.load(json_open)[0]

    # print(json_load)

    label = json_load["http://www.w3.org/2000/01/rdf-schema#label"][0]["@value"]

    '''
    start = json_load["https://jpsearch.go.jp/term/property#start"][0]["@value"]
    start_s = start.split("-")

    end = json_load["https://jpsearch.go.jp/term/property#end"][0]["@value"]
    end_s = end.split("-")
    '''

    description = ""

    if "http://schema.org/description" in json_load:
        description = json_load["http://schema.org/description"][0]["@value"]

    image = ""

    if "http://schema.org/image" in json_load:
        image = json_load["http://schema.org/image"][0]["@id"]

    

    birthDate = ""
    sib = ""
    children = ""

    if os.path.exists(file.replace("entity", "test")):

        path = file.replace("entity", "test")

        json_open2 = open(path, 'r')
        json_load2 = json.load(json_open2)

        for obj in json_load2:
            if obj["@id"] == json_load["@id"]:
                print(obj)

                if "http://ja.dbpedia.org/property/兄弟" in obj:
                    arr = []
                    for a in obj["http://ja.dbpedia.org/property/兄弟"]:
                        a = a["@id"].split("/chname/")[1].split(".")[0]
                        arr.append(a)

                    sib = "|".join(arr)

                if "http://ja.dbpedia.org/property/子" in obj:
                    arr = []
                    for a in obj["http://ja.dbpedia.org/property/子"]:
                        a = a["@id"].split("/chname/")[1].split(".")[0]
                        arr.append(a)

                    children = "|".join(arr)

                if "https://jpsearch.go.jp/term/property#start" in obj:
                    arr = []
                    for a in obj["https://jpsearch.go.jp/term/property#start"]:
                        a = a["@value"]
                        arr.append(a)

                    birthDate = "|".join(arr)
                    


        # print(json_load)



    rows.append([label, description, image, birthDate, sib, children, "https://w3id.org/hi/snorql/?describe=https%3A%2F%2Fw3id.org%2Fhi%2Fapi%2Fentity%2Fchname%2F"+label])

with open('data/p.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)