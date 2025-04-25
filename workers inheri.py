class Worker:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def compute_pay(self, hours):
        return 0

class DailyWorker(Worker):
    def compute_pay(self, hours):
        return self.rate * hours

class SalariedWorker(Worker):
    def compute_pay(self, hours):
        return self.rate * 40  # fixed 40 hours per week

# Input for Daily Worker
name1 = input("Enter daily worker: ")
hours1 = int(input("Enter working hours: "))
rate1 = int(input("Enter salary: "))

# Input for Salaried Worker
name2 = input("\nEnter salaried worker: ")
hours2 = int(input("Enter working hours: "))
rate2 = int(input("Enter salary: "))

# Creating objects
daily_worker = DailyWorker(name1, rate1)
salaried_worker = SalariedWorker(name2, rate2)

# Display output
print(f"\n{daily_worker.name}'s pay is: {daily_worker.compute_pay(hours1)}")
print(f"{salaried_worker.name}'s pay is: {salaried_worker.compute_pay(hours2)}")
