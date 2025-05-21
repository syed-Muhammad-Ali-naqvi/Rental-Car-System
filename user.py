
## Users

from models import Person
from utils import console, get_valid_choice

############
# User class
###########
class User(Person):
    def __init__(self, name, system):
        super().__init__(name)
        self.system = system

    def menu(self):
        while True:
            try:
                console.print(f"\n[bold cyan]User Menu ({self.name}):[/bold cyan]")
                console.print("1. Rent a Car\n2. Return a Car\n3. Show Available Cars\n4. Show All Cars\n5. Show Balance\n6. Deposit Funds\n7. View Activity Log\n8. Back to Main Menu")
                choice = get_valid_choice("Choose an option: ", ["1","2","3","4","5","6","7","8"])
                if choice == "1":
                    self.system.rent_car(self.name)
                elif choice == "2":
                    self.system.return_car(self.name)
                elif choice == "3":
                    self.system.show_available_cars()
                elif choice == "4":
                    self.system.show_all_cars()
                elif choice == "5":
                    self.system.show_user_balance(self.name)
                elif choice == "6":
                    try:
                        amount = float(input("Enter amount to deposit: ").strip())
                        self.system.deposit_funds(self.name, amount)
                    except:
                        console.print("[red]❌ Invalid amount.[/red]")
                elif choice == "7":
                    self.system.show_user_activity(self.name)
                elif choice == "8":
                    break


        except KeyboardInterrupt:
            console.print("\n[yellow]Operation interrupted by user. Returning to main menu...[/yellow]")
            continue 

        except Exception as e:
            console.print(f"[red]An unexpected error occurred: {e}[/red]")

