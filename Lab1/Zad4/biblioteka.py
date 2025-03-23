class Ksiazka:

    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"Tytul: {self.tytul}  Autor:{self.autor} Rok wydania: {self.rok_wydania}"


class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return super().opis() + " Rozmiar pliku: " + str(self.rozmiar_pliku)

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return super().opis() + " Czas trwania: " + str(self.czas_trwania)