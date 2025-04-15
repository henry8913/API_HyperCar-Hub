import json
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
from pathlib import Path

app = FastAPI(title="HyperCar-Hub API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Modello dati per le auto
class Car(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    brand: str
    price: float
    imageUrl: str


# File di storage JSON
STORAGE_FILE = "cars.json"


# Funzioni di utilità per la gestione del file JSON
def load_cars():
    if Path(STORAGE_FILE).exists():
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    return []


def save_cars(cars):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(cars, f, indent=2)


@app.get("/")
def read_root():
    return {
        "name": "HyperCar-Hub API",
        "version": "1.0",
        "endpoints": {
            "GET /cars": "Lista tutte le auto",
            "GET /cars/{id}": "Ottieni auto specifica",
            "POST /cars": "Aggiungi una nuova auto",
            "POST /cars/bulk": "Aggiungi multiple auto",
            "PUT /cars/{id}": "Aggiorna un'auto",
            "DELETE /cars/{id}": "Elimina un'auto"
        }
    }


@app.get("/cars", response_model=List[Car])
def get_cars():
    return load_cars()


@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: str):
    cars = load_cars()
    for car in cars:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Auto non trovata")


@app.post("/cars", response_model=Car)
def create_car(car: Car):
    cars = load_cars()
    car.id = str(uuid.uuid4())
    cars.append(car.dict())
    save_cars(cars)
    return car


@app.post("/cars/bulk", response_model=List[Car])
def create_cars(cars: List[Car]):
    existing_cars = load_cars()
    new_cars = []
    for car in cars:
        car.id = str(uuid.uuid4())
        car_dict = car.dict()
        existing_cars.append(car_dict)
        new_cars.append(car)
    save_cars(existing_cars)
    return new_cars


@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: str, updated_car: Car):
    cars = load_cars()
    for i, car in enumerate(cars):
        if car["id"] == car_id:
            updated_car.id = car_id
            cars[i] = updated_car.dict()
            save_cars(cars)
            return updated_car
    raise HTTPException(status_code=404, detail="Auto non trovata")


@app.delete("/cars/{car_id}")
def delete_car(car_id: str):
    cars = load_cars()
    for i, car in enumerate(cars):
        if car["id"] == car_id:
            del cars[i]
            save_cars(cars)
            return {"message": "Auto eliminata con successo"}
    raise HTTPException(status_code=404, detail="Auto non trovata")
