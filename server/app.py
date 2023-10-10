# Importez les modules nécessaires
from fastapi import FastAPI, HTTPException
from cassandra.cluster import Cluster

# Créez une instance FastAPI
app = FastAPI()

# Initialisez la connexion à Cassandra
cluster = Cluster(['172.21.0.2'])  # Mettez les noms de vos conteneurs Cassandra ici
session = cluster.connect('resto')  # Remplacez 'resto' par le nom de votre keyspace Cassandra

# Définissez les endpoints de l'API

# Endpoint pour obtenir les informations d'un restaurant par son ID
@app.get("/restaurant/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    # Exécutez une requête CQL pour obtenir les informations du restaurant
    result = session.execute(f"SELECT * FROM restaurant WHERE id = {restaurant_id}")
    restaurant = result.one()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

# Endpoint pour récupérer la liste des noms de restaurants par type de cuisine
@app.get("/restaurants-by-cuisine/{cuisine_type}")
def get_restaurants_by_cuisine(cuisine_type: str):
    # Exécutez une requête CQL pour obtenir les noms des restaurants par type de cuisine
    result = session.execute(f"SELECT name FROM restaurant WHERE cuisinetype = '{cuisine_type}'ALLOW FILTERING;")
    restaurants = [row.name for row in result]
    return restaurants

# Endpoint pour obtenir le nombre d'inspections d'un restaurant par son ID
@app.get("/inspection-count/{restaurant_id}")
def get_inspection_count(restaurant_id: int):
    # Exécutez une requête CQL pour obtenir le nombre d'inspections pour un restaurant
    result = session.execute(f"SELECT COUNT(*) FROM inspection WHERE idrestaurant = {restaurant_id}")
    count = result.one()
    if not count:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return count[0]

@app.get("/top-10-restaurants-by-grade/{grade}")
def get_top_10_restaurants_by_grade(grade: str):
    if not session:
        return {f"message": "Erreur de connexion à Cassandra"}
    query = f"SELECT * FROM inspection WHERE grade = '{grade}' LIMIT 10 ALLOW FILTERING;"
    result = session.execute(query)
    restaurants = []
    for row in result:
        # récup l'id du restaurant à partir de la colonne "idrestaurant" de la table d'inspection
        restaurant_id = row.idrestaurant
        restaurant_query = f"SELECT * FROM restaurant WHERE id = {restaurant_id}"
        restaurant_result = session.execute(restaurant_query)
        restaurant_data = restaurant_result.one()
        if restaurant_data:
            restaurant_dict = {
                "id": restaurant_data.id,
                "name": restaurant_data.name,
                "cuisine_type": restaurant_data.cuisinetype,
                "grade": row.grade,
            }
            restaurants.append(restaurant_dict)
    if restaurants:
        return restaurants
    else:
        return {f"message": "Aucun restaurant trouvé pour ce type de grade"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
