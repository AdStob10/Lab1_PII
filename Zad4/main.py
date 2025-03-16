import biblioteka as b
if __name__ == "__main__":
    e1 = b.Ebook("Winds Of Truth", "Brandon Sanderson", 2024, 110)
    a1 = b.Audiobook("Inne Pieśni", "Jacek Dukaj", 2002, 560)
    print(e1.opis())
    print(a1.opis())