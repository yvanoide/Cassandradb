# Cassandradb


ReadMe - Projet Cassandra pour l'Inspection des Restaurants
Introduction
Ce projet vise à répondre aux besoins d'un client en matière de gestion et d'inspection de restaurants en utilisant la base de données NoSQL Cassandra. Le client souhaite centraliser les résultats des inspections des restaurants dans une base de données évolutive et résiliente. L'objectif est de démontrer la faisabilité du projet en déployant un cluster Cassandra, en créant une API pour accéder aux données et en utilisant des conteneurs Docker pour faciliter le déploiement.

Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

Docker (version 24.0.6 ou supérieure)
Docker Compose (version 1.29.2 ou supérieure)
Git (pour cloner le dépôt du projet)
Instructions d'Installation
Clonez ce dépôt GitHub sur votre machine.

Accédez au répertoire du projet.

Construisez et lancez les conteneurs Docker à l'aide de Docker Compose.

docker compose up -d
Cela créera un cluster Cassandra avec 2 nœuds et lancera l'application FastAPI pour accéder aux données.

Note : Assurez-vous d'obtenir l'adresse IP du conteneur Cassandra cassandra-node1 à l'aide de la commande docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cassandra-node1. Utilisez cette adresse IP pour configurer la connexion à Cassandra dans l'application FastAPI (voir le fichier app.py).

Utilisation de l'Application
Accédez à l'interface utilisateur Streamlit à l'adresse http://localhost:8501 dans votre navigateur pour visualiser les données des restaurants et des inspections.

L'API FastAPI est accessible à l'adresse http://localhost:8000. Vous pouvez interagir avec l'API en utilisant des requêtes HTTP pour obtenir des informations sur les restaurants et les inspections.

Maintenance et Nettoyage
Pour arrêter et supprimer les conteneurs Docker, exécutez la commande suivante dans le répertoire du projet.


docker compose down
Livrables
Lien vers le GitHub du projet contenant le docker-compose pour le cluster Cassandra, le code de l'API FastAPI, la documentation et les démonstrations des tests de l'API.
Remarques
Ce projet est un exemple d'utilisation de Cassandra pour gérer les données d'inspection des restaurants. Vous pouvez l'adapter et l'élargir en fonction de vos besoins spécifiques. Amusez-vous bien avec ce projet de gestion de données à grande échelle !
