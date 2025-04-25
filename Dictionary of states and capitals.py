# Dictionary of states and capitals
states_and_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield"
}

# Ask user to input a state
state = input("Enter a state: ")

# Display the capital of the state if it's in the dictionary
if state in states_and_capitals:
    print(f"The capital of {state} is {states_and_capitals[state]}.")
else:
    print("State not found in the dictionary.")
