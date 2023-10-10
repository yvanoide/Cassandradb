from fastapi import FastAPI, HTTPException
from cassandra.cluster import Cluster

app = FastAPI()

# Initialisez la connexion Cassandra
cassandra_host = "172.18.0.2"  # Remplacez par l'adresse IP de votre nœud Cassandra
cassandra_keyspace = "resto"
cluster = Cluster([cassandra_host])
session = cluster.connect(cassandra_keyspace)

# Requête pour trouver les informations d'un restaurant à partir de son ID
@app.get("/restaurant/{restaurant_id}")
async def get_restaurant_info(restaurant_id: int):
    query = "SELECT * FROM restaurant WHERE id = %s"
    rows = session.execute(query, (restaurant_id,))
    restaurant_info = rows.one()
    if restaurant_info is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    return {"restaurant_info": dict(restaurant_info)}


# Requête pour la liste des noms de restaurants à partir de son type de cuisine
@app.get("/restaurants-by-cuisine/{cuisine_type}")
async def get_restaurants_by_cuisine(cuisine_type: str):
    query = f"SELECT name FROM restaurant WHERE cuisinetype = '{cuisine_type}'"
    rows = session.execute(query)
    restaurant_names = [row.name for row in rows]
    return {"restaurant_names": restaurant_names}

# Requête pour le nombre d'inspections d'un restaurant à partir de son ID
@app.get("/restaurant-inspection-count/{restaurant_id}")
async def get_inspection_count(restaurant_id: int):
    query = "SELECT COUNT(*) FROM inspection WHERE idrestaurant = %s"
    rows = session.execute(query, (restaurant_id,))
    inspection_count = rows.one()[0]
    return {"inspection_count": inspection_count}


# Requête pour les noms des 10 premiers restaurants à partir d'un grade donné
@app.get("/top-10-restaurants-by-grade/{grade}")
async def get_top_10_restaurants_by_grade(grade: str):
    query = "SELECT name FROM restaurant WHERE grade = %s LIMIT 10"
    rows = session.execute(query, (grade,))
    restaurant_names = [row.name for row in rows]
    return {"top_10_restaurants": restaurant_names}


# Fermez la connexion Cassandra à la fin de l'application
@app.on_event("shutdown")
async def shutdown_event():
    cluster.shutdown()
