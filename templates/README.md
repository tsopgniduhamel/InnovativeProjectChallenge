# Innovative Projects Challenge

Dans le cadre de la compétition **Innovative Projects Challenge**, nous avons décidé de réaliser le projet **TakeCare237** qui vise à mettre sur pied une application web qui intègre un modèle de Machine Learning.

Le but de l'application web est d'indiquer à un patient (au vue de ses paramètres corporels) s'il peut

- rester en observation,
- aller en soins intensifs ou
- rentrer chez lui

Nous avons testé plusieurs modèles sur notre jeu de données et nous avons retenu le modèle avec la plus grande précision

- **Decision Tree:** Accuracy= **76.8 %**
- **Random Forest:** Accuracy= **79.1 %**
- **AdaBoost:** Accuracy= **55.6 %**
- **KNN:** Accuracy= **87.5 %**
- **MLP - neural network:** Accuracy= **88.8 %**
- **Naive Bayes:** Accuracy= **38.9 %**
- **Logistic Regression:** Accuracy= **70.2 %**
- **Support Vector Machines:** Accuracy= **88.7 %**
- **Linear SVC:** Accuracy= **70.2 %**
- **Stochastic Gradient Descent (SGD):** Accuracy= **68.8 %**

Le modèle final retenu est : + **MLPClassifier(random_state=90, max_iter=250)** + dont la **précision** est : 0.894 soit **89.4%**

L'application web finale a été développée avec [Flask](https://flask.palletsprojects.com/en/1.1.x/) et déployée sur [Heroku](https://dashboard.heroku.com/)

**Auteurs**

- [Tsopgni Duhamel](https://github.com/tsopgniduhamel)
- [Tchazou Fabrice](https://github.com/fabrice17p035)
