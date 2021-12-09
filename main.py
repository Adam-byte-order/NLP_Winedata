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

    x = dataset.taster_name.values
    y = dataset[['taster_name']].values


    lb = preprocessing.LabelEncoder()
    dataset.loc[:, 'taster_name_encoded'] = lb.fit_transform(y)

    # Text Analysis begins :
    comment_taster = text_data
    comment_taster.isna().sum()  # handling missing values for taster
    # testing whether we can get any data by overlapping and comparing the twitter handler and taster name
    taster = []
    taster_id = []
    ind1 = comment_taster[comment_taster['taster_name'].isna() == True].index
    ind2 = comment_taster[comment_taster['taster_twitter_handle'].isna() == True].index
    common = set(ind1).intersection(set(ind2))
    print(len(common))
    comment_taster.drop(common, axis=0, inplace=True)
    ind3 = comment_taster[comment_taster['taster_twitter_handle'].isna() == True].index
    print(len(ind3))
    comment_taster.drop('taster_twitter_handle', axis=1, inplace=True)


    x = comment_taster.taster_name.values
    y = comment_taster[['taster_name']].values
    lb = preprocessing.LabelEncoder()
    comment_taster.loc[:, 'taster_name_encoded'] = lb.fit_transform(y)


    taster_and_code = comment_taster.loc[:, ['description', 'taster_name', 'taster_name_encoded']]
    comment_taster.drop('taster_name', axis=1, inplace=True)


    # Text Normalization and preprocessing
    j = 0
    lemmatiser = WordNetLemmatizer()

    for i in comment_taster.loc[:, 'description'].index:
        final_out = ' '
        sent = comment_taster.loc[i, 'description']
        j = j + 1
        # punctuation check
        sentence1 = [char for char in sent if char not in string.punctuation]
        sentence = ''.join(sentence1)
        # lower case conversion
        temp1 = sentence.lower()
        # splitting
        temp = temp1.split()
        # stopwords removal
        words = [word for word in temp if word not in stopwords.words('english')]
        # lemmetizing the sentence
        for word in words:
            b = lemmatiser.lemmatize(word, pos="v")
            final_out = final_out + b + ' '

        comment_taster.loc[i, 'description'] = final_out

