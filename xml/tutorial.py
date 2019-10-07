
# https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

tree = ET.parse('assets/country_data.xml')
root = tree.getroot()

print(root.tag)

for child in root:
    print(child.tag, child.attrib)