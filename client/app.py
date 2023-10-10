# Importez les modules nécessaires
import streamlit as st
import requests

# Définissez l'URL de l'API FastAPI côté serveur
server_url = "http://localhost:8000"  

# Page d'accueil de l'application Streamlit
st.title("Restaurant Data App")

# Sidebar pour sélectionner une fonctionnalité
option = st.sidebar.selectbox("Sélectionnez une fonctionnalité", ["Obtenir les informations d'un restaurant", "Liste des restaurants par type de cuisine", "Nombre d'inspections d'un restaurant", "Top 10 restaurants par grade"])

# Fonction pour obtenir les informations d'un restaurant par ID
def get_restaurant_by_id():
    restaurant_id = st.text_input("Entrez l'ID du restaurant")
    if st.button("Obtenir les informations"):
        response = requests.get(f"{server_url}/restaurant/{restaurant_id}")
        if response.status_code == 200:
            restaurant_data = response.json()
            if restaurant_data:
                # Afficher les informations du restaurant
                st.write("Informations du restaurant :")
                st.write(f"ID : {restaurant_data[0]}")  # Utilisez l'index pour accéder aux éléments de la liste
                st.write(f"Nom : {restaurant_data[1]}")
                st.write(f"grade : {restaurant_data[2]}")
                # ... (ajoutez d'autres informations ici)
            else:
                st.error("Restaurant non trouvé")
        else:
            st.error("Erreur lors de la récupération des données du restaurant")



# Fonction pour obtenir la liste des restaurants par type de cuisine
def get_restaurants_by_cuisine():
    cuisine_type = st.text_input("Entrez le type de cuisine")
    if st.button("Obtenir la liste"):
        response = requests.get(f"{server_url}/restaurants-by-cuisine/{cuisine_type}")
        if response.status_code == 200:
            restaurants = response.json()
            st.write(restaurants)
        else:
            st.error("Aucun restaurant trouvé pour ce type de cuisine")

# Fonction pour obtenir le nombre d'inspections d'un restaurant par ID
def get_inspection_count():
    restaurant_id = st.text_input("Entrez l'ID du restaurant")
    if st.button("Obtenir le nombre d'inspections"):
        response = requests.get(f"{server_url}/inspection-count/{restaurant_id}")
        if response.status_code == 200:
            count = response.json()
            st.write(f"Nombre d'inspections : {count}")
        else:
            st.error("Restaurant non trouvé")

# Fonction pour obtenir les noms des 10 premiers restaurants par grade
def get_top_10_restaurants_by_grade():
    grade = st.text_input("Entrez le grade")
    if st.button("Obtenir le top 10"):
        response = requests.get(f"{server_url}/top-10-restaurants-by-grade/{grade}")
        if response.status_code == 200:
            restaurants = response.json()
            st.write(restaurants)
        else:
            st.error("Aucun restaurant trouvé pour ce grade")

# Affichez la fonctionnalité sélectionnée
if option == "Obtenir les informations d'un restaurant":
    get_restaurant_by_id()
elif option == "Liste des restaurants par type de cuisine":
    get_restaurants_by_cuisine()
elif option == "Nombre d'inspections d'un restaurant":
    get_inspection_count()
elif option == "Top 10 restaurants par grade":
    get_top_10_restaurants_by_grade()
