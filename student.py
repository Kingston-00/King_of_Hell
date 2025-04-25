class Students:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print("Average Marks:", self.calculate_average())

# Example Usage
s1 = Students("Alice", 101)
s1.add_marks("Math", 85)
s1.add_marks("Science", 90)
s1.add_marks("English", 80)
s1.display_details()
