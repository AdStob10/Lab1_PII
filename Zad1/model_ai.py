import json

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
            j = json.loads(f.read())
            #linie = f.readlines()[1:-1]
            name = j["name"]
            version = j["version"]
            return cls(name, version)

