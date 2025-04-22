
# API_HyperCar-Hub 🚗

Una API REST per gestire un database di auto di lusso. Questo progetto può essere utilizzato come base per creare la tua API personalizzata.

<p align="center">
  <img src="img/cover_c.jpg" alt="Cover" width="100%" />
</p>

## 📋 Descrizione
Questa API permette di gestire un catalogo di auto con operazioni CRUD complete. È sviluppata con FastAPI, un moderno framework web Python che garantisce alte prestazioni e facilità d'uso.

## 🚀 Caratteristiche
- Gestione completa CRUD per le auto
- ID random univoci per ogni auto
- Supporto per caricamento singolo e multiplo
- Validazione automatica dei dati con Pydantic
- Documentazione interattiva con Swagger UI
- Storage persistente in JSON
- CORS abilitato per integrazione frontend

## ⚙️ Installazione e Avvio

### Prerequisiti
- Python 3.10 o superiore
- pip (gestore pacchetti Python)

### Clona la Repository
1. Clona la repository:
```bash
git clone https://github.com/henry8913/API_HyperCar-Hub.git
```
2. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

### Avvio Server
```bash
uvicorn main:app --host 0.0.0.0 --reload
```

## 🛠️ Struttura Progetto
```
├── main.py           # File principale dell'API
├── pyproject.toml    # Configurazione progetto e dipendenze
└── requirements.txt  # Dipendenze Python
```

## 📡 API Reference

### Endpoints Base
- `GET /` - Info API e endpoints disponibili

### Endpoints Auto
- `GET /cars` - Lista tutte le auto
- `GET /cars/{id}` - Ottieni auto specifica
- `POST /cars` - Aggiungi una nuova auto
- `POST /cars/bulk` - Aggiungi multiple auto
- `PUT /cars/{id}` - Aggiorna un'auto
- `DELETE /cars/{id}` - Elimina un'auto

### Formato Dati Auto
```json
{
    "name": "Nome Auto",
    "description": "Descrizione dell'auto",
    "brand": "Marca",
    "price": 100000,
    "imageUrl": "URL dell'immagine"
}
```

## 🔄 Persistenza e Test

### Storage Dati
I dati vengono salvati in un file `cars.json` che viene creato automaticamente.

### Test API
Puoi testare l'API tramite:
- Swagger UI: `/docs`
- ReDoc: `/redoc`
- Qualsiasi client HTTP (Postman, curl, fetch)

## 👤 Guida alla Personalizzazione

### Modifica del Modello Dati
1. Apri `main.py`
2. Trova la classe `Car` e modificala secondo le tue esigenze:
```python
class TuoModello(BaseModel):
    id: int | None = None
    campo1: str
    campo2: int
    campo3: float
    # Aggiungi altri campi necessari
```

### Personalizzazione Endpoints
1. Modifica i nomi degli endpoints nel codice:
```python
@app.get("/tuoi-dati")  # invece di /cars
@app.post("/aggiungi")  # invece di /cars
```

### Personalizzazione Storage
1. Modifica `STORAGE_FILE` per cambiare il file di storage:
```python
STORAGE_FILE = "tuo_file.json"
```

### Aggiunta Nuove Funzionalità
1. Aggiungi nuovi endpoints per funzionalità specifiche:
```python
@app.get("/ricerca/{termine}")
def cerca(termine: str):
    # Implementa la tua logica di ricerca
    pass
```

### Personalizzazione Risposte
1. Modifica il formato delle risposte API:
```python
@app.get("/")
def read_root():
    return {
        "nome_api": "La Tua API",
        "versione": "1.0",
        "endpoints": {
            # Lista dei tuoi endpoints
        }
    }
```

## 🔐 Sicurezza
- Implementa autenticazione per ambiente di produzione
- Considera l'uso di rate limiting
- Valida input utente (già implementato con Pydantic)

## 📚 Contributi e Licenza

### 🤝 Contributi
Sentiti libero di fare fork e migliorare il progetto!

### 👤 Autore
Progetto creato da [Henry](https://github.com/henry8913).

### 📝 Licenza
Distribuito sotto la licenza [MIT](https://github.com/henry8913/API_HyperCar-Hub/blob/main/LICENSE.txt). Consulta il file `LICENSE` per maggiori dettagli.
