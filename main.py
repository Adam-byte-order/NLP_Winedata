from sklearn.datasets import make_regression
import numpy as np
import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats
import time
import datetime
from nltk.stem import WordNetLemmatizer
import string
from sklearn.model_selection import train_test_split
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
# nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer



# Funcio per a llegir dades en format csv
def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset


if __name__ == '__main__':
    # Carreguem dataset
    dataset = load_dataset('Winery.csv')
    # print(dataset.info())

    # Dropping usless "Unnamed: 0" column
    dataset.drop('Unnamed: 0', axis='columns', inplace=True)

    # Separating the text data that will be preprocessed
    text_data = dataset.loc[:, ['description', 'taster_name', 'taster_twitter_handle']]

    # handling missing values:

    # Check nulls
    # print(dataset.isna().sum())
    # print("handling missing values:")
    dataset.dropna(subset=["taster_name"], inplace=True)
    dataset.dropna(subset=["designation"], inplace=True)
    dataset.dropna(subset=["region_1"], inplace=True)
    dataset["price"].fillna(dataset["price"].mean, inplace=True)
    #print(dataset.isna().sum())

    # Data visualization
    #dataset.groupby('country').winery.count().plot.bar()
    #plt.show()
    #sns.boxplot(x='country', y='points', data=dataset)
    #plt.show()
    #dataset['points'].hist()
    #plt.show()

    # label encoding for the taster name :
    lb = preprocessing.LabelEncoder()
    dataset.loc[:, 'taster_name_encoded'] = lb.fit_transform(dataset.taster_name.values)

    Y = dataset['taster_name_encoded']
    X = dataset['description']
    # Training and test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    print("Shape of train predictors", X_train.shape)
    print("Shape of test predictors", X_test.shape)

    # Wordmatrix with TF-IDF
    from sklearn import feature_extraction

    td = feature_extraction.text.TfidfVectorizer()
    word_train = td.fit_transform(X_train)
    word_test = td.transform(X_test)

    from sklearn.linear_model import LogisticRegression
    text_model_lr = LogisticRegression(max_iter = 1000).fit(word_train, Y_train)

    from sklearn.naive_bayes import MultinomialNB
    text_model_nb = MultinomialNB().fit(word_train, Y_train)

    y_predict_lr = text_model_lr.predict(word_test)
    y_predict_nb = text_model_nb.predict(word_test)

    accuracy_lr = np.mean(y_predict_lr == Y_test)
    accuracy_nb = np.mean(y_predict_nb == Y_test)
    print("Accuracy of Logistic Model ==", accuracy_lr)
    print("Accuracy of Naives Model ==", accuracy_nb)
