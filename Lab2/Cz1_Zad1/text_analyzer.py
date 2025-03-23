class TextAnalyzer:

    @staticmethod
    def word_count(text):
        return len(text.split())

    @staticmethod
    def char_count(text):
        return len(text)

    @staticmethod
    def unique_words(text):
        return len(set(text.split()))