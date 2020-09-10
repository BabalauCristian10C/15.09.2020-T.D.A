cvul = {"Numele, Prenumele: " : "Cristian Babalau", "Data nasterii: " :"09.11.04", "Clase terminate: " : "9"}
note = {'Informatica: ': 9 ,'Biologie: ': 8 , 'Matematica:': 8.36}

i = 0

for obiecte_note in note:
    i += 1
    print(i, 'Nota la',obiecte_note , note[obiecte_note], )

i = 0
print()

for datele in cvul:
    i += 1
    print(datele, cvul[datele])

print(type(cvul))
print(len(cvul))
