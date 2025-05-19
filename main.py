
## Main
## Run it on Command Prompt

from utils import intro_sequence, console, get_valid_choice
from system import RentalSystem
from admin import Admin
from user import User
from constant import ADMIN_CREDENTIALS
from getpass import getpass


############
# Main
###########
def main():
    system = RentalSystem()
    intro_sequence()
    while True:
        console.print("\n[bold magenta]Main Menu:[/bold magenta]")
        console.print("1. Admin Login\n2. User Login\n3. Register a User\n4. Show All Cars\n5. Exit")
        choice = get_valid_choice("Choose an option: ", ["1","2","3","4","5"])
        if choice == "1":
            username = input("Enter Admin Username: ").strip()
            password = getpass("Enter Password: ")
            if ADMIN_CREDENTIALS.get(username) == password:
                admin = Admin(username, system)
                admin.menu()
            else:
                console.print("[red]❌ Invalid Admin credentials.[/red]")
        elif choice == "2":
            username = input("Enter Username: ").strip()
            password = getpass("Enter Password: ")
            if username in system.users and system.users[username]["password"] == password:
                user = User(username, system)
                user.menu()
            else:
                console.print("[red]❌ Invalid User credentials.[/red]")
        elif choice == "3":
            system.register_user()
        elif choice == "4":
            system.show_all_cars()
        elif choice == "5":
            console.print("[bold red]Exiting the program. Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()