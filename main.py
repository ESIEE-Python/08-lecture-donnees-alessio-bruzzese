"""Fonction qui permet de retourner les vaeurs d'un csv"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers."""
    l = []
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            l = [list(map(int, line.strip().split(';'))) for line in lines]
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' est introuvable.")
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste dans les données."""
    return data[k] if 0 <= k < len(data) else []

def get_first(l):
    """Retourne le premier élément de la liste."""
    return l[0] if l else None

def get_last(l):
    """Retourne le dernier élément de la liste."""
    return l[-1] if l else None

def get_max(l):
    """Retourne le maximum de la liste."""
    return max(l) if l else None

def get_min(l):
    """Retourne le minimum de la liste."""
    return min(l) if l else None

def get_sum(l):
    """Retourne la somme des éléments de la liste."""
    return sum(l) if l else 0

#### Fonction principale

def main():
    """fonction prncipale"""
    # Lecture des données
    data = read_data(FILENAME)
    # Affichage des données lues
    if data:
        for i, l in enumerate(data):
            print(f"Ligne {i + 1}: {l}")
        # Test des fonctions sur une liste particulière
        k = 0  # Modifier l'indice k pour tester d'autres listes
        liste_k = get_list_k(data, k)
        if liste_k:
            print(f"\nListe {k + 1}: {liste_k}")
            print("Premier élément:", get_first(liste_k))
            print("Dernier élément:", get_last(liste_k))
            print("Maximum:", get_max(liste_k))
            print("Minimum:", get_min(liste_k))
            print("Somme:", get_sum(liste_k))
        else:
            print(f"Aucune liste à l'indice {k}.")
    else:
        print("Aucune donnée à afficher.")

if __name__ == "__main__":
    main()
