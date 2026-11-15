
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from division import divide_numbers
import csv
import os

app = FastAPI(title="Division API")

os.makedirs("data", exist_ok=True)

class DivisionInput(BaseModel):
    num: float
    denominator: float


def save_input(num, denominator):
    file_path = "data/current.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["num", "denominator"])

        writer.writerow([num, denominator])


@app.get("/")
def home():
    return {"message": "Division API is running"}


@app.post("/divide")
def division(data: DivisionInput):

    if data.denominator == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )

    result = divide_numbers(data.num, data.denominator)

    save_input(data.num, data.denominator)

    return {
        "numerator": data.num,
        "denominator": data.denominator,
        "result": result
    }
