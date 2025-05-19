# Car Rental Management System

## 1. Problem Description
The Car Rental Management System is designed to facilitate the process of renting and returning vehicles. It enables users to view available cars, rent a vehicle for a specified number of days, and return the vehicle while managing user balances and inventory. The system aims to streamline the car rental process, ensure accurate tracking of available cars, and handle user transactions efficiently.

## 2. Distinguishing Features of the Project

### Features:
- User registration and login  
- Viewing available cars  
- Renting a car with duration specification  
- Returning a rented car  
- Managing user balances  
- Tracking total available cars in inventory  


# 🧠 Object-Oriented Programming Concepts

This project demonstrates key OOP concepts through various classes and their interactions:

| Concept            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Abstraction**    | The `Person` class is an abstract base class using `@abstractmethod`, serving as a blueprint for `User` and `Admin` classes, defining common behaviors without implementation. |
| **Inheritance**    | `User` and `Admin` classes inherit from the `Person` abstract class, gaining shared properties and methods, enabling code reuse and hierarchical organization. |
| **Polymorphism**   | Both `User` and `Admin` classes override the `menu()` method, allowing different menu options and behaviors depending on the user type, even when accessed via a `Person` reference. |
| **Encapsulation**  | Class attributes like `name`, `balance`, and `car_id` are encapsulated within classes. Data access is controlled via methods, protecting internal state from unintended modifications. |
| **Composition**    | The `RentalSystem` class is composed of multiple objects such as `Car` instances and user data structures, managing their interactions to implement system functionalities. |



## 3. Flow of the Project

### Flow:
1. User logs in or registers.
2. User views available cars.
3. User selects a car and specifies rental duration.
4. System checks inventory and user balance.
5. If valid, system processes rental, updates inventory and user balance.
6. User can return the car, updating inventory and balance.

--- 

## 4. Most Challenging Part for Me While Working on the Project
The most challenging part was managing the synchronization between the car inventory and user rental status. Ensuring that the available cars decrease correctly when rented and increase when returned - without messing up the flow - took careful class coordination and logic checks.

---

## 5. Any New Thing Learned in Python While Working on the Project
I leveled up in OOP! Learned how to create classes, use constructors, apply encapsulation, and structure code more cleanly. Also got better at handling user input and simulating real-world processes like rentals.

---

## 6. Individual Contributions of Each Member in the Project

- **Muhammad Ali (CS-24134):** Designed the class structure, implemented `User` and `Car` classes, and handled user registration and login functionalities.
- **Umer Iqbal (CS-24127):** Developed the rental and return process, managed inventory updates, and created the user interface.
- **Rameel Ahmed (CS-24126):** Tested the system, documented the flow, and prepared the report and screenshots.

---

## 7. Future Expansions
- Add inheritance and different pricing models for car types.
- Implement a graphical user interface (GUI).
- Integrate a database for persistent storage.
- Allow for advance reservations and dynamic pricing.
- Include email/SMS alerts for due dates and offers.

---

## How to Use the System

### Prerequisites:
- Python 3.x installed on your system.
- Programming style: Object Oriented Programming.
- The project files (Python scripts) available in your working directory.

### Running the Program:
1. Open your terminal or command prompt.
2. Navigate to the directory containing the Python files.

   ```bash
   cd path/to/your/project/directory
   python main.py
