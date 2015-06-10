#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/return/disproportional.html

# The photo has a link to http://www.pythonchallenge.com/pc/phonebook.php. The error page led me to xml rpc.
import xmlrpc.client as client

server = client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# print(server.system.listMethods())
# print(server.system.methodSignature('phone'))
# print(server.system.methodHelp('phone'))
print(server.phone('Bert'))
