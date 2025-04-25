class Sport:
    def __init__(self, name, players, equipment):
        self.name = name
        self.players = players
        self.equipment = equipment

# List of sports
sports = [
    Sport("Football", "11 players", ("Ball", "Goalposts")),
    Sport("Basketball", "5 players", ("Ball", "Basket")),
    Sport("Cricket", "11 players", ("Bat", "Ball")),
    Sport("Tennis", "1 or 2 players", ("Racket", "Ball"))
]

# Search input
search_name = input("Enter sport: ").lower()

# Search and display
for sport in sports:
    if search_name in sport.name.lower():
        print(f"{sport.name}: {sport.players}, Equipment: {sport.equipment}")
        break
else:
    print("Sport not found.")
