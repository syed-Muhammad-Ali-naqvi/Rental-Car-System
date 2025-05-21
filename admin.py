
## Admin

from models import Person
from utils import console, get_valid_choice

##################
# Class Admin
#################
class Admin(Person):
    def __init__(self, name, system):
        super().__init__(name)
        self.system = system

    def menu(self):
        try:
            while True:
                console.print("\n[bold yellow]Admin Menu:[/bold yellow]")
                console.print("1. Show all cars\n2. Show available cars\n3. Add new car\n4. View activity logs\n5. Register new user\n6. Show all users\n7. Back to Main Menu")
                choice = get_valid_choice("Choose an option: ", ["1","2","3","4","5","6","7"])
                if choice == "1":
                    self.system.show_all_cars()
                elif choice == "2":
                    self.system.show_available_cars()
                elif choice == "3":
                    self.system.add_car()
                elif choice == "4":
                    self.system.show_logs()
                elif choice == "5":
                    self.system.register_user()
                elif choice == "6":
                    self.system.show_users()
                elif choice == "7":
                    break


        except KeyboardInterrupt:
            console.print("\n[yellow]Operation interrupted by user. Returning to main menu...[/yellow]")
            continue  

        except Exception as e:
            console.print(f"[red]An unexpected error occurred: {e}[/red]")

