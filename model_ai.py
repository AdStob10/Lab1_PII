class ModelAI:

    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja_modelu):
        self.nazwa_modelu = nazwa_modelu
        self.wersja_modelu = wersja_modelu
        self.nowy_model()


    def nowy_model(self):
        ModelAI.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, mode="r") as f:
            linie = f.readlines()[1:-1]
            name = linie[0].strip().split(" ")
            version = linie[1].strip().split(" ")
            cls(name[1][1:-1], version[1])

