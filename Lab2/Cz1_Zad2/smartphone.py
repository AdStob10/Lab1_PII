import telefon
import komunikacja
import rozrywka
class Smartphone(telefon.Telefon, rozrywka.Rozrywka, komunikacja.Komunikacja):
    def __init__(self, model, producent):
        super().__init__(model, producent)
        