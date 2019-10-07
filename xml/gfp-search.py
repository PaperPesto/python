import json, xml.etree.ElementTree as ET

# Fattura eredita da object
class Fattura(object):
    def __init__(self, idFattura, nomefile):
        self.idFattura = idFattura
        self.nomefile = nomefile
    def getInfo(self):
        return self.idFattura + ' ' + self.nomefile

tree = ET.parse('assets/getFattureDaElaborare_22-24-MAG.xml')
root = tree.getroot()

# array raw di fatture
rawfatture = root[0][0][0]

# array di oggetti fattura
fatture = []

for child in rawfatture:
    filename = child[7].text
    idFattura = child[9].text
    fatture.append(Fattura(idFattura, filename))

for f in fatture:
    print(f.getInfo())