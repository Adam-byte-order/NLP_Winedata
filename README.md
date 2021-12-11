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
### Model
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, XX | 57% | 100ms |
| Random Forest | 1000 Trees, XX | 58% | 1000ms |
| SVM | kernel: lineal C:10 | 58% | 200ms |
| -- | -- | -- | -- |
| [model de XXX](link al kaggle) | XXX | 58% | ?ms |
| [model de XXX](link al kaggle) | XXX | 62% | ?ms |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
El millor model que s'ha aconseguit ha estat...
En comparació amb l'estat de l'art i els altres treballs que hem analitzat....
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
