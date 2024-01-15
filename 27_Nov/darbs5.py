with open ('zem.txt', 'r' encoding='utf8') as datne:
    teksts=datne.read()
    print(f"failā ir šads teksts: {teksts}")
skaits=len(teksts)
print(f"simbolu skaits tekstā ir {skaits}.")

print(f"pirmie desmit simboli ir: {teksts[:10]}")
print(f"pirmais un pēdējais simbols ir: {teksts[0]} {teksts[len(teksts)-1]}")
