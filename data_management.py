
## Data Management

import os
import json
import csv
from utils import console, get_current_time
from models import Car
from constant import FILENAME, FIELDNAMES, USERDATA_FILE

def load_users():
    if not os.path.exists(USERDATA_FILE):
        default_data = {
            "admin": {
                "password": "admin123",
                "balance": 0.0,
                "activity_log": [f"{get_current_time()} - Admin account created."]
            }
        }
        with open(USERDATA_FILE, 'w') as f:
            json.dump(default_data, f)
        console.print(f"[blue]Created default user data file '{USERDATA_FILE}'.[/blue]")
        return default_data
    else:
        try:
            with open(USERDATA_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            console.print(f"[red]Error reading {USERDATA_FILE}. Creating default data.[/red]")
            default_data = {
                "admin": {
                    "password": "admin123",
                    "balance": 0.0,
                    "activity_log": [f"{get_current_time()} - Admin account created."]
                }
            }
            with open(USERDATA_FILE, 'w') as f:
                json.dump(default_data, f)
            return default_data

def save_users(users):
    try:
        with open(USERDATA_FILE, 'w') as f:
            json.dump(users, f, indent=4)
    except Exception as e:
        console.print(f"[red]Error saving users: {e}[/red]")

def load_cars():
    cars = []
    if not os.path.exists(FILENAME):
        # Load default cars if file missing
        console.print("[yellow]Cars file not found. Loading default cars.[/yellow]")
        default_cars = [
            Car("C001", "Model S", "Tesla", "2020", "100", 2),
            Car("C002", "Mustang", "Ford", "2018", "80", 3),
            Car("C003", "Civic", "Honda", "2019", "50", 5),
            Car("C004", "Corolla", "Toyota", "2017", "45", 4),
            Car("C005", "Accord", "Honda", "2021", "60", 3),
            Car("C006", "Camry", "Toyota", "2019", "55", 2),
            Car("C007", "Model 3", "Tesla", "2021", "110", 2),
            Car("C008", "Charger", "Dodge", "2019", "90", 1),
            Car("C009", "SUV X", "XUV", "2020", "120", 2),
            Car("C010", "Ranger", "Ford", "2016", "70", 4),
        ]
        return default_cars
    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if all(field in row and row[field].strip() != '' for field in FIELDNAMES):
                    try:
                        car = Car(
                            row["Car ID"],
                            row["Model"],
                            row["Brand"],
                            row["Year"],
                            row["Rent Per Day"],
                            row["Available"]
                        )
                        cars.append(car)
                    except Exception as e:
                        print(f"Error parsing row: {row} - {e}")
    except Exception as e:
        print(f"Error loading cars: {e}")
    return cars

def save_cars(cars):
    try:
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            for car in cars:
                writer.writerow(car.to_dict())
        console.print(f"[green]Car data saved to '{FILENAME}'.[/green]")
    except Exception as e:
        console.print(f"[red]Error saving cars: {e}[/red]")