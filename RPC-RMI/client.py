import xmlrpc.client

MY_SERVER = "http://localhost:5000"

cpf_number = input("Type a CPF number: ")

with xmlrpc.client.ServerProxy(MY_SERVER) as proxy:
    if proxy.validate_cpf(cpf_number):
        print("CPF is valid :)")
    else:
        print("CPF is invalid :(")
