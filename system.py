
## System

from datetime import datetime
from utils import console, get_current_time
from models import Car
from data_management import load_cars, save_cars, load_users, save_users
from rich.table import Table

#########################
# Rental system class
#########################
class RentalSystem:
    def __init__(self):
        self.cars = load_cars()
        self.users = load_users()
        self.rental_sessions = {}

    def load_users(self):
        self.users = load_users()

    def save_users(self):
        save_users(self.users)

    def load_cars(self):
        self.cars = load_cars()

    def save_cars(self):
        save_cars(self.cars)

    def show_all_cars(self):
        if not self.cars:
            console.print("[yellow]⚠️ No cars in inventory.[/yellow]")
            return
        table = Table(title="All Cars")
        for field in ["Car ID", "Model", "Brand", "Year", "Rent Per Day", "Available"]:
            table.add_column(field)
        for car in self.cars:
            table.add_row(*[str(car.to_dict()[field]) for field in ["Car ID", "Model", "Brand", "Year", "Rent Per Day", "Available"]])
        console.print(table)

    def show_available_cars(self):
        available_cars = [car for car in self.cars if car.available > 0]
        if available_cars:
            from rich.table import Table
            table = Table(title="Available Cars")
            for field in ["Car ID", "Model", "Brand", "Year", "Rent Per Day", "Available"]:
                table.add_column(field)
            for car in available_cars:
                table.add_row(*[str(car.to_dict()[field]) for field in ["Car ID", "Model", "Brand", "Year", "Rent Per Day", "Available"]])
            console.print(table)
        else:
            console.print("[red]No cars currently available for rent.[/red]")

    def add_car(self):
        from rich.prompt import Prompt
        try:
            car_id = Prompt.ask("Enter Car ID").strip()
            if any(c.car_id == car_id for c in self.cars):
                console.print("[red]❌ Car ID already exists![/red]")
                return
            model = Prompt.ask("Enter Model").strip()
            brand = Prompt.ask("Enter Brand").strip()
            year = Prompt.ask("Enter Year").strip()
            rent_input = Prompt.ask("Enter Rent Per Day").strip()
            available_input = Prompt.ask("Enter Number of Cars Available").strip()

            if not (model and brand and year.isdigit() and rent_input.isdigit() and available_input.isdigit()):
                console.print("[red]❌ All fields must be filled correctly with valid numbers.[/red]")
                return

            new_car = Car(car_id, model, brand, year, rent_input, int(available_input))
            self.cars.append(new_car)
            self.save_cars()
            console.print("[green]✔ Car added successfully![/green]")
        except Exception as e:
            console.print(f"[red]❌ Failed to add car: {e}[/red]")

    def rent_car(self, username):
        self.show_available_cars()

        from rich.prompt import Prompt


        while True:
            car_id = Prompt.ask("Enter Car ID to rent").strip()

            car = next((c for c in self.cars if c.car_id == car_id), None)
            if not car:
                console.print(f"[red]❌ Car ID '{car_id}' not found. Please enter a valid Car ID.[/red]")
                continue
            if car.available <= 0:
                console.print(f"[yellow]⚠️ Sorry, Car ID '{car_id}' is not available right now.[/yellow]")
                return
            break


        while True:
            days_input = Prompt.ask("Enter number of days to rent").strip()
            try:
                days = int(days_input)
                if days <= 0:
                    console.print("[red]❌ Number of days must be greater than zero. Please try again.[/red]")
                    continue
                break
            except:
                console.print("[red]❌ Invalid input for number of days. Please enter a valid number.[/red]")

        total_cost = car.rent * days
        user_balance = self.users[username]["balance"]
        if user_balance < total_cost:
            console.print("[red]❌ Insufficient balance to rent this car.[/red]")
            return


        self.users[username]["balance"] -= total_cost
        car.available -= 1
        self.save_cars()
        self.save_users()
        self.log_activity(username, f"Rented {car.model} ({car.car_id}) for {days} days, paid ${total_cost}")
        console.print(f"[green]Successfully rented {car.model} for {days} days. Paid ${total_cost}[/green]")
        self.rental_sessions[username] = {
            "car_id": car.car_id,
            "start_time": get_current_time(),
            "agreed_days": days
        }
    def return_car(self, username):
        session = self.rental_sessions.get(username)
        if not session:
            console.print("[red]No active rental session found.[/red]")
            return
        car_id = session["car_id"]
        start_time_str = session["start_time"]
        agreed_days = session["agreed_days"]
        car = next((c for c in self.cars if c.car_id == car_id), None)
        if not car:
            console.print("[red]Car data not found.[/red]")
            return
        start_dt = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        now_dt = datetime.now()
        days_stayed = (now_dt - start_dt).days
        if days_stayed < 1:
            days_stayed = 1

        base_cost = car.rent * days_stayed
        extra_days = max(0, days_stayed - agreed_days)
        extra_cost = 0
        if extra_days > 0:
            extra_cost = car.rent * (extra_days * 0.5)
            console.print(f"[yellow]Extra days: {extra_days}. Extra charge: ${extra_cost}[/yellow]")

        total_cost = base_cost + extra_cost

        if self.users[username]["balance"] < extra_cost:
            console.print("[red]Insufficient balance to cover extra charges.[/red]")
            return
        self.users[username]["balance"] -= extra_cost

        car.available += 1
        self.save_cars()
        self.save_users()
        self.log_activity(username, f"Returned {car.model} after {days_stayed} days, paid additional ${extra_cost}")
        console.print(
            f"[green]Return processed. Total charge: ${total_cost}. Extra charges: ${extra_cost}. Total balance now: ${self.users[username]['balance']}[/green]")
        del self.rental_sessions[username]

    def register_user(self):
        from rich.prompt import Prompt
        username = input("Enter a new username: ").strip()
        if not username:
            console.print("[red]❌ Username cannot be empty.[/red]")
            return
        if username in self.users:
            console.print(f"[red]❌ Username '{username}' already exists![/red]")
            return
        from getpass import getpass
        password = getpass("Enter a new password: ")
        try:
            initial_balance = float(Prompt.ask("Enter initial deposit (wallet balance)").strip())
        except:
            console.print("[red]❌ Invalid amount. Registration aborted.[/red]")
            return
        self.users[username] = {
            "password": password,
            "balance": initial_balance,
            "activity_log": [f"{get_current_time()} - Account created with initial balance ${initial_balance}"]
        }
        self.save_users()
        console.print(f"[green]✔ User '{username}' registered successfully with balance ${initial_balance}[/green]")

    def show_user_balance(self, username):
        balance = self.users[username]["balance"]
        console.print(f"[bold]Current balance for {username}: ${balance:.2f}[/bold]")
        self.log_activity(username, f"Checked wallet balance: ${balance:.2f}")

    def deposit_funds(self, username, amount):
        self.users[username]["balance"] += amount
        self.save_users()
        self.log_activity(username, f"Deposited ${amount:.2f}")
        console.print(f"[green]Deposited ${amount:.2f} from your registered credit card. New balance: ${self.users[username]['balance']:.2f}[/green]")

    def log_activity(self, username, activity):
        timestamp = get_current_time()
        entry = f"{timestamp} - {activity}"
        self.users[username]["activity_log"].append(entry)
        self.save_users()

    def show_user_activity(self, username):
        logs = self.users[username]["activity_log"]
        console.print(f"[bold underline]Activity Log for {username}:[/bold underline]")
        for log in logs:
            console.print(log)

    def show_logs(self):
        for username, data in self.users.items():
            console.print(f"\n[bold]Activity Log for {username}:[/bold]")
            for log in data.get("activity_log", []):
                console.print(log)

    def show_users(self):
        if not self.users:
            console.print("[yellow]No users found.[/yellow]")
            return
        from rich.table import Table
        table = Table(title="Users")
        table.add_column("Username")
        table.add_column("Password")
        table.add_column("Balance")
        for username, data in self.users.items():
            balance = data.get("balance", 0.0)
            password = data.get("password", "")
            table.add_row(username, password, f"${balance:.2f}")
        console.print(table)