from model_ai import ModelAI
if __name__ == "__main__":
    ModelAI.z_pliku("test.json")
    ModelAI.z_pliku("test2.json")
    print(f"Ile modeli: {ModelAI.ile_modeli()}")