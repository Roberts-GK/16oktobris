#lietotāja ievadīto tekstu un aprēķiniet burtu un vārdu skaitu tajā.

#Lietotāja ievadītais teksts
teksts=input("Ievadi tekstu:")



#aprēķināt burtu skaitu ... kā programma zinās ka tas ir burts?
#isalpha()
burtuskaits=0
for burts in teksts:
    if burts.isaplha():
        burtuskaits+=1 #burtu skaits ir vienads ar burtu skaitu +1
  




#sadalīt tekstu pa vārdiem
vardi=teksts.split() #atdalītājs split(",")



# aprēķināt vārdu skaitu




varduskaits=len(vardi)
#IZVADĪT REZULTĀTU
print(f"burtu skaits ir {burtuskaits}")
print(f"vardu skaits ir {varduskaits}")