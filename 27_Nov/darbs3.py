"""
rakstīt/veidot datnes

"""
fails=open('aka.txt', "a", encoding='utf8')
fails.write("šodien sniegs ir pamaz..")
fails.close()

#atvērt un nolasīt
ff=open('aste.txt', 'r', encoding='utf8')
print(ff.read())

#Izveidot jaunu tukšu failu
gg=open('ziema.txt', 'x')
kk=open("vasara.txt", 'w')

#dzēšana
import os
os.remove('ziema.txt')