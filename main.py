import os

import pandas as pd
from cgitb import text
from logging import root
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional, Text
from enum import Enum

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'DATA')

dataset = os.path.join(DATA_DIR, 'circuits.csv')
app = FastAPI()


@app.get("/")
def read_root():
    return{"Bienvenido: al Himalaya"}

@app.get("/circuitos")
def dataset_circuitos_obtener():
    df = pd.read_csv(dataset)
    return df.to_dict()







