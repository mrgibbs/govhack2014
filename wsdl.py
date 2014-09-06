# -*- coding: utf-8 -*-
__author__ = 'roman'
import codecs
import xml.etree.ElementTree as ET
from suds.client import Client

#f = codecs.open("U20.xml","w+",'utf-8')
#client = Client("http://testwl.irc.gov.ua:7003/EDRAPI/ws?WSDL")
#f.write(client.service.plsqlSearchByCode("38890891", 2, "10000035", "10000035", None ,None))
tree = ET.parse('U7.xml')
root = tree.getroot()
for name in root.iter('NAME'):
    for value in name.attrib.values():
        if (value == u"Назва КВЕД"):
            print(name.text)
for name in root.iter('ATU_NAME'):
    for value in name.attrib.values():
        print(name.text)






