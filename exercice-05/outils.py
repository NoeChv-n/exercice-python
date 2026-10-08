def convertir_note(texte):
    """
    Convertit un texte à virgule en un nombre flottant.
    """
    if "," in texte:
        texte = texte.replace(",", ".")
    try:
        return float(texte)
    except ValueError:
        return None

convertir_note("12.5")  # Retourne 12.5

def moyenne(valeur):
    """
    Calcule la moyenne d'une liste de valeurs.
    """
    if not valeur:
        return None
    return sum(valeur) / len(valeur)

def mention(note):
    """
    Retourne la mention correspondant à une note.
    """
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


