from model_ai import ModelAI
if __name__ == "__main__":
    test = ModelAI.z_pliku("Zad1/test.json")
    ModelAI.z_pliku("Zad1/test2.json")
    print(f"Ile modeli: {ModelAI.ile_modeli()}")