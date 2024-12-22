# Projet de Détection des URL de Phishing

Ce projet est conçu pour détecter les URL de phishing. Le backend utilise des techniques de machine learning pour analyser les caractéristiques des URL et prédire si elles sont malveillantes.

## Fonctionnement du Projet

### Backend

Le backend est développé en Python avec Flask. Il utilise plusieurs bibliothèques pour le traitement des données et le machine learning.

#### Fonctionnalités Principales

- Extraction des caractéristiques des URL : Le script extrait diverses caractéristiques des URL telles que la présence d'une adresse IP, la longueur de l'URL, l'utilisation de services de raccourcissement d'URL, etc.
- Prétraitement des données : Les données sont normalisées et les valeurs manquantes sont imputées.
- Modèle de Machine Learning : Un modèle de classification RandomForest est utilisé pour prédire si une URL est un phishing ou non.

### Frontend

Le frontend est développé en React.js. Il permet aux utilisateurs de soumettre des URL pour analyse et affiche les résultats de la prédiction.

## Comment le Projet Détecte le Phishing

Le cœur de ce projet est un modèle de machine learning entraîné à différencier les URL légitimes des URL de phishing en se basant sur un ensemble de 30 caractéristiques extraites des URL. Ces caractéristiques incluent des éléments tels que la longueur de l'URL, la présence de caractères spéciaux, le statut SSL, l'âge du domaine, et plus encore. En examinant ces attributs, le modèle apprend à identifier les schémas et comportements courants dans les tentatives de phishing.

### Caractéristiques Clés pour Détecter le Phishing

La première étape pour construire un système de détection de phishing est de comprendre ce qui rend une URL ou un email suspect.

Bien que le design soit souvent très similaire à celui du site légitime, nous nous concentrons sur des caractéristiques quantitatives :

1. **having_IP_Address:** Les URL contenant une adresse IP au lieu d'un nom de domaine sont souvent suspectes.
2. **URL_Length:** Les URL plus longues peuvent indiquer des tentatives d'obfuscation de la véritable destination d'un lien.
3. **Shortening_Service:** Les URL raccourcies peuvent cacher des adresses malveillantes, les rendant plus difficiles à détecter.
4. **having_At_Symbol:** La présence de "@" dans une URL peut être utilisée pour tromper les utilisateurs et les amener à visiter des sites malveillants.
5. **double_slash_redirecting:** Les redirections suivant "//" peuvent parfois être un signe de phishing.
6. **Prefix_Suffix:** Un tiret ("-") dans un nom de domaine peut indiquer une version factice d'un site légitime.
7. **having_Sub_Domain:** Un grand nombre de sous-domaines peut indiquer des tentatives d'imitation d'un site légitime.
8. **SSLfinal_State:** Les certificats SSL valides sont courants sur les sites légitimes ; les sites de phishing n'en ont souvent pas.
9. **Domain_registeration_length:** Les périodes d'enregistrement courtes peuvent indiquer une utilisation temporaire et frauduleuse.
10. **Favicon:** Utiliser un favicon différent ou le charger depuis une source externe peut être suspect.
11. **port:** Les sites légitimes utilisent généralement des ports standards ; des ports inhabituels peuvent être suspects.
12. **HTTPS_token:** Certains sites de phishing incluent "https" dans leurs noms de domaine pour paraître légitimes.
13. **Request_URL:** Vérifier si des éléments (comme des images) sont hébergés sur des sites externes peut détecter le phishing.
14. **URL_of_Anchor:** Les sites de phishing utilisent souvent des balises d'ancrage avec des URL trompeuses.
15. **Links_in_tags:** Similaire à "Request_URL", mais vérifie les balises meta, script et link pour des liens malveillants.
16. **SFH (Server Form Handler):** Si les données de formulaire sont envoyées à un domaine différent, cela peut indiquer du phishing.
17. **Submitting_to_email:** Les formulaires utilisant "mailto:" peuvent indiquer des tentatives de phishing.
18. **Abnormal_URL:** Une structure d'URL qui dévie de la norme peut être suspecte.
19. **Redirect:** Les sites de phishing utilisent souvent plusieurs redirections pour masquer la destination finale.
20. **on_mouseover:** Changer le comportement (par exemple, la barre d'état) au survol peut être une tactique de phishing.
21. **RightClick:** Désactiver le clic droit peut empêcher les utilisateurs d'inspecter ou de copier le lien.
22. **popUpWidnow:** Les fenêtres pop-up peuvent être utilisées pour tromper les utilisateurs et les amener à entrer des informations personnelles.
23. **Iframe:** Les iframes cachées peuvent indiquer des tentatives de masquer du contenu malveillant.
24. **age_of_domain:** Les domaines plus récents sont plus susceptibles d'être utilisés pour le phishing.
25. **DNSRecord:** Les sites de phishing peuvent manquer de dossiers DNS valides ou avoir des informations incohérentes.
26. **web_traffic:** Un trafic plus faible suggère qu'un site pourrait être moins fiable.
27. **Page_Rank:** Les sites avec un PageRank faible peuvent être moins légitimes.
28. **Google_Index:** Les sites de phishing peuvent ne pas être indexés par Google, indiquant un manque de légitimité.
29. **Links_pointing_to_page:** Les sites de phishing peuvent avoir peu de backlinks ou de liens externes.
30. **Statistical_report:** Utiliser des bases de données de sites de phishing connus peut aider à la détection.

Ces caractéristiques nous donnent des indices sur la sécurité d'une URL ou d'un email. Voyons maintenant comment nous pouvons apprendre à une IA à utiliser ces indices.

### Le Jeu de Données et son Prétraitement

Le jeu de données contient 102816 visites web et 30 caractéristiques ont été enregistrées pour chacune des visites. De plus, une valeur de classe a été attribuée à chaque enregistrement.

### Construction de Notre IA : Différentes Approches

Les algorithmes de machine learning suivants ont été utilisés et évalués :
1. **Régression Logistique**
2. **Régression par Arbre de Décision**
3. **Classificateur Random Forest**
4. **Machine à Vecteurs de Support (SVM)**

Après avoir expérimenté ces modèles, le **Classificateur Random Forest** s'est avéré être le plus précis, atteignant une précision et un rappel de 96,7% et une exactitude de 97%.

Le projet inclut également une API RESTful construite avec Flask, permettant aux utilisateurs de saisir une URL et de recevoir une prédiction sur la sécurité potentielle de l'URL.

## Le projet contient deux pages :

Page d'Accueil :
La page d'accueil présente l'objectif du projet et permet aux utilisateurs de saisir une URL.

![image](https://github.com/user-attachments/assets/3135dd5b-2ce7-4344-869b-0f279fb2b739)

Page de Résultats :
La page de résultats donne le résultat en indiquant si l'URL est un spam ou non :

![image](https://github.com/user-attachments/assets/c61a6a69-38b5-489d-878a-b11e3b166f85)

## Comment exécuter le projet :

Frontend avec React.js :

```sh
npm start.
```

Backend with Flask:

```sh
#Créez un environnement virtuel et activez-le.

python -m venv venv.

source venv/bin/activate.

#Installez les dépendances en utilisant pip install -r requirements.txt.

pip install -r requirements.txt.

#Exécutez python app.py pour démarrer le serveur Flask.

python app.py.
```
# Phishing_URL
