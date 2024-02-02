from typing import List, Dict, Any
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific origins
    allow_credentials=True,
    allow_methods=["*"],  # You can replace "*" with specific HTTP methods
    allow_headers=["*"],  # You can replace "*" with specific headers
)

def db_connection(database_path: str):
    return sqlite3.connect(database_path)

def map_column(column_names: List[str], row: tuple):
    return dict(zip(column_names, row))

@app.get("/get/", response_model=List[Dict[str, Any]])
def get_all_warframes(
    id: int = Query(None, description="Warframe ID"),
    name: str = Query(None, description="Warframe name"),
    gender: str = Query(None, description="Warframe gender"),
    release_date: str = Query(None, description="Warframe release date"),
    primed_date: str = Query(None, description="Prime version release date"),
    price_platinum: int = Query(None, description="Warframe price in Platinum"),
    warframe_type: str = Query(None, description="Warframe type"),
    start_date: str = Query(None, description="Start Date (YYYY-MM-DD)"),
    end_date: str = Query(None, description="End Date (YYYY-MM-DD)"),
):
    conn = db_connection("database.sqlite")
    cursor = conn.cursor()

    # Build the SQL query based on the provided conditions
    query = "SELECT * FROM warframes WHERE 1=1"
    params = []

    if id is not None:
        query += " AND id = ?"
        params.append(id)

    if name:
        query += " AND name = ?"
        params.append(name)

    if gender:
        query += " AND gender = ?"
        params.append(gender)

    if release_date:
        query += " AND release_date = ?"
        params.append(release_date)

    if primed_date:
        query += " AND primed_date = ?"
        params.append(primed_date)

    if price_platinum is not None:
        query += " AND price_platinum = ?"
        params.append(price_platinum)

    if warframe_type:
        query += " AND warframe_type = ?"
        params.append(warframe_type)

    if start_date and end_date:
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
        query += " AND release_date BETWEEN ? AND ?"
        params.extend([start_datetime, end_datetime])

    # Execute the query
    cursor.execute(query, params)
    data = cursor.fetchall()

    # Map numeric indices to column names
    column_names = ["id", "name", "gender", "release_date", "primed_date", "price_platinum", "warframe_type"]
    result = [map_column(column_names, row) for row in data]

    return result
