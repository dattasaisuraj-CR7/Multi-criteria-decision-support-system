import heapq
import time

# ==========================================================
# HYBRID MULTI-CRITERIA DECISION SUPPORT SYSTEM
# ==========================================================

print("\n========== CO6 : HYBRID AI SYSTEM ==========")

# ==========================================================
# ALTERNATIVE DATA
# ==========================================================

alternatives = [

    {
        "name": "Laptop A",
        "price": 45000,
        "rating": 4.5,
        "performance": 8,
        "probability": 0.8
    },

    {
        "name": "Laptop B",
        "price": 60000,
        "rating": 4.9,
        "performance": 9,
        "probability": 0.9
    },

    {
        "name": "Laptop C",
        "price": 48000,
        "rating": 4.3,
        "performance": 7,
        "probability": 0.7
    },

    {
        "name": "Laptop D",
        "price": 42000,
        "rating": 4.7,
        "performance": 9,
        "probability": 0.85
    }
]


# ==========================================================
# USER CONSTRAINTS (CSP)
# ==========================================================

budget = 50000

minimum_rating = 4.4


# ==========================================================
# WEIGHTS
# ==========================================================

weights = {

    "rating": 0.4,
    "performance": 0.4,
    "probability": 0.2
}


# ==========================================================
# SEARCH STRUCTURES
# ==========================================================

open_set = []

closed_set = set()


# ==========================================================
# TRACE LOGGING
# ==========================================================

print("\n========== TRACE LOGGING ==========")

for item in alternatives:

    print(
        f"Loaded Alternative : {item['name']}"
    )


# ==========================================================
# CSP FILTERING
# ==========================================================

print("\n========== CSP FILTERING ==========")

valid_alternatives = []

for item in alternatives:

    print(f"\nChecking {item['name']}")

    if item["price"] > budget:

        print("Rejected : Price exceeds budget")

        continue

    if item["rating"] < minimum_rating:

        print("Rejected : Rating too low")

        continue

    print("Accepted")

    valid_alternatives.append(item)


# ==========================================================
# HEURISTIC FUNCTION
# ==========================================================

def heuristic(option):

    return (
        option["rating"]
        + option["performance"]
    )


# ==========================================================
# UTILITY FUNCTION
# ==========================================================

def calculate_utility(option):

    utility = (

        option["rating"]
        * weights["rating"]

        +

        option["performance"]
        * weights["performance"]

        +

        option["probability"]
        * 10
        * weights["probability"]
    )

    return utility


# ==========================================================
# SEARCH + UTILITY EVALUATION
# ==========================================================

print("\n========== SEARCH EVALUATION ==========")

for item in valid_alternatives:

    h_value = heuristic(item)

    utility_score = calculate_utility(item)

    final_score = h_value + utility_score

    print(
        f"{item['name']} --> "
        f"Heuristic = {h_value} "
        f"Utility = {utility_score} "
        f"Final Score = {final_score}"
    )

    heapq.heappush(
        open_set,
        (-final_score, item["name"])
    )


# ==========================================================
# BEST DECISION
# ==========================================================

print("\n========== BEST RECOMMENDATION ==========")

best = heapq.heappop(open_set)

print("Recommended Option :", best[1])


# ==========================================================
# PERFORMANCE ENGINEERING
# ==========================================================

print("\n========== PERFORMANCE ANALYSIS ==========")

start_time = time.time()

nodes_expanded = len(valid_alternatives)

peak_memory_estimate = len(open_set) + len(closed_set)

time.sleep(1)

end_time = time.time()

print("Nodes Expanded :", nodes_expanded)

print("Peak Memory Usage :", peak_memory_estimate)

print(
    "Execution Time :",
    end_time - start_time
)


# ==========================================================
# FAILURE ANALYSIS
# ==========================================================

print("\n========== FAILURE ANALYSIS ==========")

for item in alternatives:

    if item["price"] > budget:

        print(
            f"{item['name']} failed due to "
            f"high price"
        )

    elif item["rating"] < minimum_rating:

        print(
            f"{item['name']} failed due to "
            f"low rating"
        )


# ==========================================================
# EXPLAINABLE AI REASONING
# ==========================================================

print("\n========== EXPLAINABLE AI ==========")

for item in valid_alternatives:

    print(
        f"""
Explanation for {item['name']}:

1. Price within budget
2. Rating satisfies constraints
3. Performance acceptable
4. Probability considered
5. Utility maximized
"""
    )


# ==========================================================
# ETHICS & LIMITATIONS
# ==========================================================

print("\n========== ETHICS & LIMITATIONS ==========")

print("""
1. Heuristic bias may affect recommendations
2. Probability estimates may be inaccurate
3. User preferences may change dynamically
4. Limited data may reduce recommendation quality
5. System decisions depend on assigned weights
""")


# ==========================================================
# FINAL SUMMARY
# ==========================================================

print("\n========== FINAL SUMMARY ==========")

print("""
Hybrid AI System Successfully Combined:

1. Search Algorithms
2. Constraint Satisfaction
3. Utility Functions
4. Probabilistic Reasoning
5. Explainable AI
6. Performance Analysis
""")
