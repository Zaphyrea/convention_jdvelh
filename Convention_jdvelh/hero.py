class Visiteur:
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
        self.charisme = self._get_initial_charisme(specialisation)

# Statistiques de départ
    def _get_initial_charisme(self, specialisation):
        if specialisation == "Cosplayeur":
            return 20
        elif specialisation == "Fan d'anime":
            return 10
        elif specialisation == "Furry":
            return 12

#Dénomination du personnage
    def get_nom(self):
        return self.name

# Suivi du charisme du personnage
    def get_charisme(self):
        return self.charisme