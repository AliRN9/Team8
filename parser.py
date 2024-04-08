import pandas as pd
import re
import spacy
import os


# python -m spacy download en


class Parser:
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    words_to_remove = [
        "a", "about", "above", "after", "again", "against", "all", "am", "an",
        "and", "any", "are", "as", "at", "be", "because", "been", "before",
        "being", "below", "between", "both", "but", "by", "can", "did", "do",
        "does", "doing", "don", "down", "during", "each", "few", "for", "from",
        "further", "had", "has", "have", "having", "he", "her", "here", "hers",
        "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is",
        "it", "its", "itself", "just", "me", "more", "most", "my", "myself",
        "no", "nor", "not", "now", "of", "off", "on", "once", "only", "or",
        "other", "our", "ours", "ourselves", "out", "over", "own", "s", "same",
        "she", "should", "so", "some", "such", "t", "than", "that", "the", "their",
        "theirs", "them", "themselves", "then", "there", "these", "they",
        "this", "those", "through", "to", "too", "under", "until", "up",
        "very", "was", "we", "were", "what", "when", "where", "which", "while",
        "who", "whom", "why", "will", "with", "you", "your", "yours", "yourself",
        "yourselves"]

    def __init__(self, path: str, lemma: bool = True) -> None:
        self.df = pd.read_csv(path)
        self.df = self.df[['Задача en', 'Обстановка en', 'Оптимальный план en', 'Предсказанный план']]
        self.df = self.df.applymap(self.remove_superfluous)
        self.df = self.df[~self.df.isin(self.words_to_remove)]
        if lemma:
            self.df = self.df.applymap(self.lemmat)
        # self.__save_csv()

    def remove_superfluous(self, sentence):
        if not isinstance(sentence, str):

            return sentence
        cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
        cleaned_sentence = re.sub(r'\n', '', cleaned_sentence)

        return cleaned_sentence

    def lemmat(self, sentence):
        if not isinstance(sentence, str):
            return sentence
        doc = self.nlp(sentence)
        return " ".join([token.lemma_ for token in doc])

    def get(self):
        return self.df

    def __save_csv(self):
        self.df.to_csv(f'{os.getcwd()}/data.csv')


if __name__ == "__main__":
    p1 = Parser('data/ИТМО_кейс_обучающая_выборка.csv', lemma=False)
    # print(p1.get())

    # p2 = Parser('data/ИТМО_кейс_обучающая_выборка.csv', lemma=False)
    # print(p2.get())
