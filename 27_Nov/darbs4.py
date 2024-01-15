"""
No termināla jautāt ievadi savu vārdu. Vārds tiek ierakstīts failā
"rudens.txt".
"""
 #lietotajam prasa ievadit savu vardu
vards=input("Ievadi savu vārdu:")
#faila nosaukums
faila_nosaukums="rudens.txt"
#mēginām atvērt failu un ierakstīt tajā vārdu
try:
    with open(faila_nosaukums, 'w') as ff:
        ff.write(vards)
        print(f"Vārds {vards} ir ierakstīts failā {faila_nosaukums}.")


except IOError:
    print(f"Kļīuda, nevarēja ierakstīt failā {faila_nosaukums}.")
