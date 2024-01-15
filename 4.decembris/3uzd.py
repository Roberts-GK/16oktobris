import json
file_name=input("ievadi datnes nosaukumu:")
try:
    with open(file_name, "r", encoding="utf8") as file:
       data=json.load(file)
except FileNotFoundError:
    print("Tādas datnes neeksistē")
except json.JSONDecodeError:
    print("Datnesformāts nav derīgs JSON.")


ziema=dict(data)

#izvadīt vārdnīcas garumu
print(f"1) Vārdnīcas garums: {len(ziema)}")