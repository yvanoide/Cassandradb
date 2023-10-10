# Utilisez l'image Streamlit officielle comme image de base
FROM streamlit/streamlit:0.90.0

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le code de votre application Streamlit dans le conteneur
COPY app.py /app

# Installez les bibliothèques nécessaires (Cassandra Driver et Pandas)
RUN pip install cassandra-driver pandas

# Exposez le port 8501 sur lequel l'application Streamlit s'exécute par défaut
EXPOSE 8501

# Commande pour exécuter l'application Streamlit lorsque le conteneur démarre
CMD ["streamlit", "run", "/app/app.py"]
