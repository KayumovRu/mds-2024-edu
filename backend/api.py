from fastapi import FastAPI
from fastapi import BackgroundTasks

from pydantic import BaseModel

import sqlite3
from backend.db import DB_PATH

from backend.ml.train import train_model
from backend.db import init_db

init_db()

app = FastAPI()

class Item (BaseModel):
    x: float
    y: float

class TrainRequest (BaseModel):
    data_path: str
    model_name: str
    train_size: float
    max_iter: int

@app.get("/")
def root():
    return {"message": "Сервер работает"}

@app.post("/sum")
def calculate_sum(item: Item):
    res = item.x + item.y
    return {"result": res}

@app.post("/train")
def train(train_request: TrainRequest):

    model_score = train_model(
        train_request.data_path,
        train_request.model_name,
        train_request.train_size,
        train_request.max_iter
    )

    return {
        "model_name": train_request.model_name,
        "train_size": train_request.train_size,
        "model_score": model_score,
        "message": "Model saved!"
    }

@app.post("/train_task")
def train_task(train_request: TrainRequest, background_tasks: BackgroundTasks):

    # model_score = train_model(
    #     train_request.data_path,
    #     train_request.model_name,
    #     train_request.train_size,
    #     train_request.max_iter
    # )

    background_tasks.add_task(
        train_model,
        train_request.data_path,
        train_request.model_name,
        train_request.train_size,
        train_request.max_iter
    )

    return {
        "model_name": train_request.model_name,
        "train_size": train_request.train_size,
        "message": "Отправлено на обучение"
    }


@app.get("/experiments")
def get_experiments():
   conn = sqlite3.connect(DB_PATH)
   cursor = conn.cursor()

   cursor.execute("""
   SELECT model_name, train_size, max_iter, score, created_at
   FROM experiments
   ORDER BY id DESC
   """)

   rows = cursor.fetchall()
   conn.close()

   experiments = []
   for row in rows:
       experiments.append({
           "model_name": row[0],
           "train_size": row[1],
           "max_iter": row[2],
           "score": row[3],
           "created_at": row[4]
       })

   return experiments