import pandas as pd
import re
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier



class Parser:
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

    def __init__(self, path: str, lemma: bool = True) -> None:
        self.df = pd.read_csv(path)
        self.df = self.df[
            ['Задача en', 'Обстановка en', 'Оптимальный план en', 'Предсказанный план', 'Успех предсказанного плана']]
        self.df = self.df.applymap(self.remove_superfluous)
        if lemma:
            self.df = self.df.applymap(self.lemmat)

    def remove_superfluous(self, sentence):
        if not isinstance(sentence, str):
            return sentence
        cleaned_sentence = re.sub(r'[.,?!"]', '', sentence.strip())
        cleaned_sentence = re.sub(r'\n', '', cleaned_sentence)
        return cleaned_sentence

    def lemmat(self, sentence):
        if not isinstance(sentence, str):
            return sentence
        doc = self.nlp(sentence)
        return " ".join([token.lemma_ for token in doc])

    def get(self):
        return self.df


class Model():
    def __init__(self, df: pd.DataFrame):
        self.xgb = XGBClassifier(learning_rate=0.1, max_depth=3, n_estimators=200)
        self.vectorizer = CountVectorizer()

        self.df = df
        self.create_dataset()
        self.vectorizers()
        self.fit()

    def create_dataset(self):
        self.X = self.df[['Задача en', 'Обстановка en', 'Оптимальный план en', 'Предсказанный план']]
        self.y = self.df['Успех предсказанного плана']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                random_state=42)

    def vectorizers(self):
        self.X_train_count = self.vectorizer.fit_transform(
            self.X_train.apply(lambda x: ' '.join(x.values.astype(str)), axis=1))
        self.X_test_count = self.vectorizer.transform(self.X_test.apply(lambda x: ' '.join(x.values.astype(str)), axis=1))

    def fit(self):
        self.xgb.fit(self.X_train_count, self.y_train)
        self.y_pred = self.xgb.predict(self.X_test_count)

    def predict(self, post_data: dict) -> dict:
        post_data = {k: [v] for k, v in post_data.items()}
        df = pd.DataFrame(post_data)
        X_test_count = self.vectorizer.transform(df.apply(lambda x: ' '.join(x.values.astype(str)), axis=1))
        print(f'{X_test_count=}')
        return self.xgb.predict(X_test_count)[0]

# if __name__== '__main__':
parser = Parser('data/ИТМО_кейс_обучающая_выборка.csv',lemma=False)  # нужно указать путь до датасета
df = parser.get()
model_ = Model(df)
