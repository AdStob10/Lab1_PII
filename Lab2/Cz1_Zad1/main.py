from advanced_text_analyzer import AdvancedTextAnalyzer
if __name__ == '__main__':
    text = "To był naprawdę wspaniały dzień!"
    print(f"Liczba słów: {AdvancedTextAnalyzer.word_count(text)}")
    print(f"Liczba znaków: {AdvancedTextAnalyzer.char_count(text)}")
    print(f"Liczba unikalnych słów: {AdvancedTextAnalyzer.unique_words(text)}")
    print(f"Analiza sentymentu: {AdvancedTextAnalyzer.sentiment_analysis(text)}")