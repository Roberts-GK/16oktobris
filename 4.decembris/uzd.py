"""
3.place() metode
"""
from tkinter import*
#izvaidojam galveno logrīku
logs=Tk()

logs.mainloop()

#kā nomainīt ikonu
logs.iconbitmap('LOGO.ico')
logs.geometry("400x300+100+50")
logs.title("Mans piermais logs")
# pievienot poas...
"""
PACK
sarkana_poga=Button(logs, text="Sarkana", fg="red")
sarkana_poga.pack(side=LEFT)
zila_poga=Button(logs, text="Zila", fg="blue")
zila_poga=Button(side=RIGHT)
zala_poga=Button(logs, text="Zaļa", fg="Green")
zala_poga.pack(side=TOP)
dzeltena_poga=Button(logs, text="Dzeltena", fg="yellow")
dzeltena_poga.pack(side=BOTTOM)
"""
"""
sarkana_poga=Button(logs, text="Sarkana", fg="red")
sarkana_poga.grid(row=0, column=2)
"""

"""
nosaukums1=Label(logs, text="Vārds").grid(row=1,column=2)
ievads1=Entry(logs).grid(row=1, column=3)
nosaukums2=Label(logs, text="uzvārds").grid(row=2,column=2)
ievads2=Entry(logs).grid(row=2, column=3)
"""
nosaukums1=Label(logs, text="Vārds").place(x=50, y=50)
ievads1=Entry(logs).place(x=95, y=50)
"""
Kādi ir logrīki:
1)uzraksts uz loga label
2)teksta ievades lauks Entry
3)poga Button
4)izvēles rūtiņa
5)izkrītošo sarakstu
6)teksta lauku
"""
logs.mainloop()