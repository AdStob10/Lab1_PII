from Lab2.Cz1_Zad1.text_analyzer import TextAnalyzer
from transformers import pipeline

class AdvancedTextAnalyzer(TextAnalyzer):
    @staticmethod
    def sentiment_analysis(text):
        sentiment_pipeline = pipeline(model="eevvgg/bert-polish-sentiment-politics")
        data = sentiment_pipeline(text)
        data.sort(key=lambda x: x["score"], reverse=True)
        return data[0]["label"]
