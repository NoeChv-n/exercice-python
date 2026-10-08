from outils import convertir_note, mention, moyenne

test = ["12,5","15","abc","9","18,25"]

note_convertie = []
nombre_notes_invalides = 0

for note in test:
    note_float = convertir_note(note)
    if note_float is not None:
        note_convertie.append(note_float)
    else :
        nombre_notes_invalides += 1

moyenne_notes = moyenne(note_convertie)
mention_notes = mention(moyenne_notes)

print("Notes converties :", note_convertie)
print("Notes ignorées :", nombre_notes_invalides)
print("Moyenne :", f"{moyenne_notes:.2f}")
print("Mention :", mention_notes)
