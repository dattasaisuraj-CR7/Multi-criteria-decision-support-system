# ==========================================================
# CSP BASED DECISION SYSTEM
# ==========================================================

laptops = [

    {
        "name": "Laptop A",
        "price": 45000,
        "rating": 4.5,
        "ram": 16,
        "storage": 512
    },

    {
        "name": "Laptop B",
        "price": 65000,
        "rating": 4.8,
        "ram": 8,
        "storage": 256
    },

    {
        "name": "Laptop C",
        "price": 40000,
        "rating": 4.1,
        "ram": 16,
        "storage": 1024
    },

    {
        "name": "Laptop D",
        "price": 48000,
        "rating": 4.7,
        "ram": 16,
        "storage": 512
    }
]


# ==========================================================
# USER CONSTRAINTS
# ==========================================================

budget = 50000

minimum_rating = 4.3

required_ram = 16


# ==========================================================
# FORWARD CHECKING
# ==========================================================

valid_options = []

print("\n========== CONSTRAINT CHECKING ==========")

for laptop in laptops:

    print(f"\nChecking : {laptop['name']}")

    if laptop["price"] > budget:

        print("Rejected : Price exceeds budget")

        continue

    if laptop["rating"] < minimum_rating:

        print("Rejected : Rating too low")

        continue

    if laptop["ram"] < required_ram:

        print("Rejected : RAM insufficient")

        continue

    print("Accepted")

    valid_options.append(laptop)


# ==========================================================
# DISPLAY VALID OPTIONS
# ==========================================================

print("\n========== VALID OPTIONS ==========")

for item in valid_options:

    print(item)


# ==========================================================
# MIN CONFLICTS
# ==========================================================

print("\n========== MIN CONFLICTS ==========")

best_option = None

least_conflicts = 999

for laptop in laptops:

    conflicts = 0

    if laptop["price"] > budget:
        conflicts += 1

    if laptop["rating"] < minimum_rating:
        conflicts += 1

    if laptop["ram"] < required_ram:
        conflicts += 1

    print(
        f"{laptop['name']} "
        f"Conflicts = {conflicts}"
    )

    if conflicts < least_conflicts:

        least_conflicts = conflicts

        best_option = laptop["name"]

print("\nBest Near Solution :", best_option)
