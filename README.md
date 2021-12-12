# Pràctica Kaggle APC UAB 2021-22
### Nom: Adam
### DATASET: Winedata
### URL: [kaggle](https://www.kaggle.com/subh86/winedata)
## Resum
El conjunt de dades ha estat sobre els comentaris o ressenyes de vins que han fet diferents tastadors de vins. Tenim 129971 dades amb 14 atributs. Un 83% d'aquests són categòrics, on comprenen atributs geogràfics com el país, la província i la regió d'origen. Després també tenim el celler, el nom del tastador i el seu Twitter. I com atributs numèrics tenim el preu i la puntuació que li han donat els tastadors.
### Objectius del dataset
El concepte principal és utilitzar la classificació de text per classificar els comentaristes a partir de les ressenyes. 
## Experiments
Durant aquesta pràctica he realitzat diferents experiments. Un cop analitzades i visualitzades les dades. He decidit provar dos tipus de mètodes per preprocessar les ressenyes dels tastadors de vins, i amb cada un d'aquests mètodes he aplicat dos entrenaments, un amb el model regressió logística i l'altre amb el naïf Bayes. També destacar que s'han fet proves d'hipermarametres en el cas del nombre màxim d'iteracions que fa la regressió logística. 
### Preprocessat
Com he esmentat anteriorment el preprocessament s'han intentat dos mètodes diferents per processar el text de les ressenyes de vins.
Aquests mètodes són molt similars i estan basats en el model bag of words. Explicat breument, segmentem cada fitxer de text en paraules i comptem el nombre de vegades que apareix cada paraula en cada document i finalment assignem a cada paraula un identificador sencer. Cada paraula única del nostre diccionari correspondrà a una característica. La llibreria sklearn te funcions que permeten crear aquesta matriu. En aquest cas hem volgut provar aquestes dues funcions: CountVectorizer() i TfidfVectorizer(). L'única diferència és que el TfidfVectorizer() retorna flotants mentre que el CountVectorizer() retorna int. I això és d'esperar: tal com s'explica a la documentació, TfidfVectorizer() assigna una puntuació mentre que CountVectorizer() compta. 
### Model
| Model | Hiperparametres | Accuracy | Temps |
| -- | -- | -- | -- |
| LogisticRegression with CountVectorizer | max_iter:50 | 96.91% | 12.38s |
| LogisticRegression with CountVectorizer | max_iter:100 | 97.75% | 24.15s |
| LogisticRegression with CountVectorizer | max_iter:500 | 97.75% | 116.63s |
| LogisticRegression with CountVectorizer | max_iter:1000 | 97.75% |  175.94s |
| LogisticRegression with CountVectorizer | max_iter:10000 | 97.75% | 193.28s |
| LogisticRegression with TfidfVectorize | max_iter:50 | 96.73% | 16.21s |
| LogisticRegression with TfidfVectorize | max_iter:100 | 97.34% | 28.89s |
| LogisticRegression with TfidfVectorize | max_iter:500 | 97.33% | 72.84s |
| LogisticRegression with TfidfVectorize | max_iter:1000 | 97.33% | 71.23s |
| LogisticRegression with TfidfVectorize | max_iter:10000 | 97.33% | 71.84s |
| Naive bayes with CountVectorizer | - | 96% | 0.130s |
| Naive bayes with TfidfVectorizer | - | 86% | 0.136s |

## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
El millor model que s'ha aconseguit ha estat la regresio logistica utilitzant previament la funcio CountVectorizer per preprocessar el text(97.75% accuracy)
En comparació amb l'unic notebook que hi ha kaggle que traballa amb el mateix dataset he pogut millorar lleugerament el valor final d'accuracy amb els dos models:
Accuracy of Logistic Model == 0.96 -> 0.97
Accuracy of Naives Model == 0.85 -> 0.96
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
