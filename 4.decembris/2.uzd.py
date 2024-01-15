import tkinter as tk
from tkinter import messagebox

def paradi_sveicienu():
    vards=ievades_lauks.get()
    messagebox.showinfo("**Sveiciens**", f"Labdien, {vards}!")
    messagebox.showinfo("Sveiciens", "Labdien, {vards}!")

#izveido galveno logu
logs=tk.Tk()
logs.title("Sveiciens lietotājam!")
logs.iconbitmap('logo.ico')
#ievades lauku vārds ievadīšanai
ievades_lauks=tk.Entry(logs, width=50)
ievades_lauks.pack(pady=10)

ievades_lauks=tk.Entry(logs, width=50)
ievades_lauks.pack(pady=10)

#poga lai izsauktu sveiciena pogu
sveiciens_poga=tk.Button(logs, text="Sveiciens")
sveiciens_poga.pack(pady=10)

#palaižam Tinker logu
logs.mainloop()