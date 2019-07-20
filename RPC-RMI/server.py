from xmlrpc.server import SimpleXMLRPCServer
from pycpfcnpj import cpfcnpj

"""
The pycpfcnpj module was developed by @matheuscas for validation
brazilian registers numbers for persons (CPF) and companies (CNPJ).
"""

server = SimpleXMLRPCServer(("localhost", 5000))
print("Listening on port 5000")
server.register_function(cpfcnpj.validate, "validate_cpf")

server.serve_forever()
