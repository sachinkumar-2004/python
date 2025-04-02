# WAP to iimplement the concept of oops of a class system which contains a child class chips.
# If the system are in the range of 70k to 100k dollar then dont be affordable
#  if it is bellow 70k and above 50k it is perfect but rest are not up to the mark.
# To store all the affordable,perfect and not up to the mark system in different new list
#  so that a user easily identify which system he wants to choose .

class System:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def categorize(self):
        """Categorizes the system based on its price."""
        if 70000 <= self.price <= 100000:
            return "Not Affordable"
        elif 50000 < self.price < 70000:
            return "Perfect"
        else:
            return "Not Up to the Mark"


class Chips(System):
    def __init__(self, name, price, chip_model):  # Fixed constructor method
        super().__init__(name, price)  
        self.chip_model = chip_model



affordable_systems = []
perfect_systems = []
not_up_to_mark_systems = []


systems = [
    Chips("System A", 45000, "Chip-X"),
    Chips("System B", 60000, "Chip-Y"),
    Chips("System C", 75000, "Chip-Z"),
    Chips("System D", 99000, "Chip-W"),
    Chips("System E", 55000, "Chip-V"),
]


for system in systems:
    category = system.categorize()
    if category == "Not Affordable":
        affordable_systems.append(system)
    elif category == "Perfect":
        perfect_systems.append(system)
    else:
        not_up_to_mark_systems.append(system)

print("\n*Perfect Systems:*")
for sys in perfect_systems:
    print(f"{sys.name} - ${sys.price} - {sys.chip_model}")

print("\n*Not Affordable Systems:*")
for sys in affordable_systems:
    print(f"{sys.name} - ${sys.price} - {sys.chip_model}")

print("\n*Not Up to the Mark Systems:*")
for sys in not_up_to_mark_systems:
    print(f"{sys.name} - ${sys.price} - {sys.chip_model}")


