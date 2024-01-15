"""
open()
kādas datnes? teksta datnes - .txt, .csv .... JSON
.txt

"""
def lasit_datni():
    # Pajautāsim ievadit datnes nosaukumu
    datnes_nosaukums=input("Ievadīt datnes nsaukumu: ")
    # Atveram failu un lasām tās saturu
    try:
        with open(datnes_nosaukums, 'r', encoding='utf-8') as fails:
            saturs=fails.read()
            print(f"Datnes saturs ir: {saturs}")



    except FileNotFoundError:
        Print("Norādīto failu nevar atrast!")
if __name__=="__main__":
    lasit_datni()