# 1 
# PEP 8 (Python Enhancement Proposal #8) Formating
# Installierung das Packet black
# in Powershell: 
# pip install black
# Verwendung:
# python -m black eine_Python_datei.py
# Z.B. 
# python -m black bedeutung.py
# Hier wird die Python-Datei nach PEP 8 formatiert. 

# Tuple
# Unterschied von List: 
# Similarities: 
# Ordered and can have duplicate or multiple values
# Differences: 
# Can not be mutated (changed)
my_tuple = (1, 2, 3)
# Indexwert wird ausgedrückt.
# Zurückgibt: 1
# mit einem Zeilenumbruch "\n"
print(my_tuple[0], "\n")
# Zurückgibt: 3
# Alternative: Zeilenumbruch mit print()
print()
print(my_tuple[2])
print()

# gibt das letzte Element zurück
# Also 3
print(my_tuple[-1])
print()

# gibt das vorletzte Element zurück
# also 2
print(my_tuple[-2])
print()

# Slicing: 
# Starte bei Index 1 (zweites Element) und nimm alles bis zum Ende
# my_tuple[1:]
print(my_tuple[1:], "\n")

# In Tuple darf man nicht das Element ändern
# Das zeigt Fehlermeldung. 
# my_tuple [1] = 144
# print(my_tuple)

# Fazit: 
# Tuple ist statisch, wenn man Tuple ändern will, 
# muss man innerhalb der Tuple die Elemente hinzufügen oder löschen. 

# Verwendung: 
# Eine Funktion kann verschiedene Werte zurückgeben.
# Z.B.: das erste Element ist eine List, und das zweite Element ist ein Boolean. 
my_tuple = ([1, 2, 3], False)
print(my_tuple, "\n")






