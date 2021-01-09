# Python-For-Data-Analysis-Projet


# But du projet

Le but de ce projet est de prédire la résiliation potentielle d'un client pour une entreprise de télécommunication iranienne. Pour cela, nous avons étudié les différents paramètres qui caractérisent la résiliation des clients.

# Dataset
Le dataset utlisé est le fichier "Customer Churn.csv".
Les données regroupent 3150 clients sélectionnés de façon aléatoire dans la base de données d'une compagnie de télécommunication iranienne sur un an.
14 variables décrivent le comportement et le statut du client avec un label churn qui sera à predire si un client va résilier ou non.

Pour plus d'informations sur le dataset:  [https://archive.ics.uci.edu/ml/datasets/Iranian+Churn+Dataset](https://archive.ics.uci.edu/ml/datasets/Iranian+Churn+Dataset)

# Machine Learning

On a découpé par la suite de notre jeu de données en un jeu d'entranement (80% = 2520 lignes) et un jeu de test (20% = 630 lignes).
Pour prédire la résiliation d'un abonnement, nous avons utilisé 5 modèles de supervisés de machine learning dans un but de classification. Ces modèles sont les suivants:
  - Regression Logistique
  - Regression Logistique (avec SMOTE)
  - Random Forest
  - KNN
  - Gradient Boosting

![Comparaison précision modèles](/images/Accuracy_result.png)

# Web App

Une API est réalisé en Python via Flask. Pour lancer l'API:

```sh
$ python3 app.py
```

Le fichier python 'request.py' permet de tester l'API en effectuant une requête avec les paramètres.
Les paramètres à envoyer sont au format JSON suivant:

{
    "values": ...
    "model": <code du modèle>
}

On peut tester des données avec les 5 modèles différents en précisant leur code.
Code des modèles:
  - LR  : Regression Logistique
  - LRS : Regression Logistique (avec SMOTE)
  - RF  : Random Forest
  - KNN : KNN
  - CLF : Gradient Boosting

