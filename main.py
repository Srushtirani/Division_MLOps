
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import csv
import os

app = FastAPI(title="Division MLOps Application")


os.makedirs("data", exist_ok=True)


def divide_numbers(num, denominator):

    if denominator == 0:
        raise ValueError("Division by zero is not allowed")

    if num < denominator:
        print("Numerator is smaller than denominator")

    return num / denominator


# Input model
class DivisionInput(BaseModel):
    num: float
    denominator: float



@app.get("/")
def home():
    return FileResponse("index.html")


# Division API
@app.post("/divide")
def division(data: DivisionInput):

    try:
        result = divide_numbers(
            data.num,
            data.denominator
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    file_path = "data/current.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["num", "denominator"])

        writer.writerow([
            data.num,
            data.denominator
        ])

    return {
        "numerator": data.num,
        "denominator": data.denominator,
        "result": result
    }


# Run Python program directly
if __name__ == "__main__":

    num = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    try:
        result = divide_numbers(num, denominator)
        print("Division =", result)

    except ValueError as e:
        print("Error:", e)
