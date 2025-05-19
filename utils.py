import os
import sys
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.03, style="bold green"):
    for char in text:
        console.print(char, end="", style=style, soft_wrap=True)
        time.sleep(delay)
    print()

def intro_sequence():
    clear()
    messages = [
        "Booting Classic Rental System...",
        "Checking car inventory...",
        "Loading user credentials...",
        "Establishing secure terminal session...",
        "Almost there..."
    ]
    for msg in messages:
        type_writer(f">> {msg}")
        time.sleep(0.5)
    time.sleep(0.5)

    # Check agreement
    if not show_agreement():
        console.print("[red]You did not accept the terms. Exiting the system...[/red]")
        sys.exit()

    clear()
    instructions = """
Welcome to the Classic Car Rental System.

Instructions:
- Choose from the menu options to Rent or Return a car.
- Check Available Cars to plan your ride.
- Admins can view activity logs and user list.
- All inputs are case-sensitive unless stated.
- Press the corresponding number to proceed.

Let's hit the road!
"""
    console.print(Panel(instructions.strip(), title="🚘 Instructions", border_style="bold magenta"))
    time.sleep(5)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        else:
            console.print(f"[red]Invalid choice '{choice}'. Please try again.[/red]")

def show_agreement():
    agreement_text = """
    Please read the following terms:
    - All rental transactions are subject to additional charges for overtime.
    - Extra charges apply if the car is returned late.
    - Admins have access to user credentials and activity logs.
    - Users must ensure their information is accurate.

    By proceeding, you agree to abide by these terms.
    """
    console.print(Panel(agreement_text, title="🚧 Agreement", border_style="bold red"))
    while True:
        response = input("Do you agree to the terms? (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            console.print("[yellow]Please type 'yes' or 'no'.[/yellow]")