import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        
        # Show BMI result
        label_result.config(text=f"Your BMI is: {bmi:.2f}")
        
        # BMI Categories
        if bmi < 18.5:
            label_category.config(text="Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            label_category.config(text="Category: Normal weight")
        elif 25 <= bmi < 29.9:
            label_category.config(text="Category: Overweight")
        else:
            label_category.config(text="Category: Obesity")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create labels, entries, and button
label_weight = tk.Label(window, text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="Enter your height (m):")
label_height.pack()

entry_height = tk.Entry(window)
entry_height.pack()

button_calculate = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack()

label_result = tk.Label(window, text="Your BMI will be displayed here.")
label_result.pack()

label_category = tk.Label(window, text="Category: ")
label_category.pack()

# Start the GUI loop
window.mainloop()
