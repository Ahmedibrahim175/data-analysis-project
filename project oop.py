class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = min(max(health_rate, 0), 100)

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = min(max(fuel_rate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        self.velocity = min(max(velocity, 0), 200)
        fuel_needed = distance

        if self.fuel_rate >= fuel_needed:
            self.fuel_rate -= fuel_needed
            remaining_distance = 0
        else:
            possible_distance = self.fuel_rate
            remaining_distance = distance - possible_distance
            self.fuel_rate = 0

        self.stop(remaining_distance)

    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance == 0:
            print("Arrived at destination.")
        else:
            print(f"Couldn't finish the trip. {remaining_distance} km left.")


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary if salary >= 1000 else 1000
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, amount):
        self.car.fuel_rate = min(self.car.fuel_rate + amount, 100)

    def send_mail(self, to, subject, body):
        print(f"Email sent to {to} | Subject: {subject}\n{body}")

    def __str__(self):
        return f"{self.name} | Mood: {self.mood} | Health: {self.health_rate} | Salary: {self.salary}"


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, emp):
        self.employees.append(emp)

    def fire(self, emp_id):
        self.employees = [e for e in self.employees if e.id != emp_id]

    def get_employee(self, emp_id):
        for e in self.employees:
            if e.id == emp_id:
                return e
        return None

    def calculate_lateness(self, arrival, expected, emp_id):
        if arrival > expected:
            minutes = (arrival - expected) * 60
            print(f"Employee #{emp_id} was late by {minutes:.0f} minutes.")
            return minutes
        else:
            print(f"Employee #{emp_id} arrived on time.")
            return 0

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount

    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount


if __name__ == "__main__":
    car = Car("Fiat 128", 100, 0)
    samy = Employee("Samy", 500, "neutral", 80, 1, car, "samy@iti.org", 3000, 20)
    office = Office("ITI Smart Village")
    office.hire(samy)

    print("\n--- distance ---")
    distance = int(input("Distance to work (km):"))
    speed = int(input("Driving speed (km/h):"))
    samy.drive(distance, speed)

    print("\n--- Arrival Time ---")
    arrival = float(input("Arrival time:"))
    expected = float(input("Expected time: "))
    office.calculate_lateness(arrival, expected, 1)

    print("\n--- Work ---")
    hours = int(input("Hours worked: "))
    samy.work(hours)
    print("Mood after work:", samy.mood)

    print("\n--- Meals ---")
    meals = int(input("Meals eaten (1-3): "))
    samy.eat(meals)
    print("Health after eating:", samy.health_rate)

    print("\n--- Summary ---")
    print(f"Name: {samy.name}")
    print(f"Salary: {samy.salary}")
    print(f"Mood: {samy.mood}")
    print(f"Health: {samy.health_rate}")
    print(f"Car fuel left: {samy.car.fuel_rate}")
