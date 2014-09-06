from suds.client import Client
url = "http://testwl.irc.gov.ua:7003/EDRAPI/ws?WSDL"
client_gov = Client(url)

print "let's start here"

result_string = client_gov.service.plsqlSearchByCode("38890933", 2, "10000035", "10000035", None, None);
print result_string