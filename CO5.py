import random

# ==========================================================
# PROBABILITY BASED DECISION SUPPORT SYSTEM
# ==========================================================

print("\n========== CO5 : PROBABILISTIC REASONING ==========")

# ==========================================================
# PRIOR PROBABILITIES
# ==========================================================

P_GoodLaptop = 0.7

P_HighRating_given_Good = 0.9

P_HighRating = 0.8


# ==========================================================
# BAYES RULE
# ==========================================================

print("\n========== BAYES RULE ==========")

P_Good_given_HighRating = (
    P_HighRating_given_Good
    * P_GoodLaptop
) / P_HighRating

print(
    "Probability that Laptop is Good "
    "Given High Rating = ",
    P_Good_given_HighRating
)


# ==========================================================
# BAYESIAN NETWORK REPRESENTATION
# ==========================================================

print("\n========== BAYESIAN NETWORK ==========")

bayesian_network = {

    "GoodLaptop": {

        "True": 0.7,
        "False": 0.3
    },

    "HighRating": {

        "GivenGood": 0.9,
        "GivenBad": 0.2
    }
}

for node in bayesian_network:

    print(node, ":", bayesian_network[node])


# ==========================================================
# EXPECTED UTILITY CALCULATION
# ==========================================================

print("\n========== EXPECTED UTILITY ==========")

laptops = [

    {
        "name": "Laptop A",
        "utility": 90,
        "probability": 0.8
    },

    {
        "name": "Laptop B",
        "utility": 70,
        "probability": 0.9
    },

    {
        "name": "Laptop C",
        "utility": 85,
        "probability": 0.6
    }
]

best_choice = None

highest_expected_utility = 0

for item in laptops:

    expected_utility = (
        item["utility"]
        * item["probability"]
    )

    print(
        f"{item['name']} "
        f"Expected Utility = "
        f"{expected_utility}"
    )

    if expected_utility > highest_expected_utility:

        highest_expected_utility = expected_utility

        best_choice = item["name"]

print("\nBest Decision :", best_choice)


# ==========================================================
# VARIABLE ELIMINATION CONCEPT
# ==========================================================

print("\n========== VARIABLE ELIMINATION ==========")

weather_probability = {

    "Sunny": 0.6,
    "Rainy": 0.4
}

purchase_probability = {

    "Sunny": 0.9,
    "Rainy": 0.5
}

total_probability = 0

for weather in weather_probability:

    value = (
        weather_probability[weather]
        * purchase_probability[weather]
    )

    print(
        f"{weather} Contribution = {value}"
    )

    total_probability += value

print(
    "\nFinal Purchase Probability =",
    total_probability
)


# ==========================================================
# MARKOV CHAIN
# ==========================================================

print("\n========== MARKOV CHAIN ==========")

states = ["Satisfied", "Unsatisfied"]

transition_matrix = {

    "Satisfied": {
        "Satisfied": 0.8,
        "Unsatisfied": 0.2
    },

    "Unsatisfied": {
        "Satisfied": 0.5,
        "Unsatisfied": 0.5
    }
}

current_state = "Satisfied"

print("Initial State :", current_state)

for day in range(1, 6):

    random_value = random.random()

    if random_value < transition_matrix[current_state]["Satisfied"]:

        current_state = "Satisfied"

    else:

        current_state = "Unsatisfied"

    print(
        f"Day {day} --> {current_state}"
    )


# ==========================================================
# SENSOR FUSION
# ==========================================================

print("\n========== SENSOR FUSION ==========")

online_review_score = 4.5

expert_review_score = 4.8

friend_recommendation_score = 4.2

final_score = (
    online_review_score * 0.4
    + expert_review_score * 0.4
    + friend_recommendation_score * 0.2
)

print("Final Combined Score =", final_score)


# ==========================================================
# SAMPLING INFERENCE
# ==========================================================

print("\n========== SAMPLING INFERENCE ==========")

success = 0

samples = 1000

for i in range(samples):

    random_value = random.random()

    if random_value < 0.7:

        success += 1

estimated_probability = success / samples

print(
    "Estimated Probability =",
    estimated_probability
)


# ==========================================================
# UNCERTAINTY AWARE DECISION
# ==========================================================

print("\n========== UNCERTAINTY DECISION ==========")

decision_options = [

    {
        "name": "Option A",
        "benefit": 90,
        "risk_probability": 0.3
    },

    {
        "name": "Option B",
        "benefit": 70,
        "risk_probability": 0.1
    }
]

best_option = None

best_value = -1

for option in decision_options:

    safe_utility = (
        option["benefit"]
        * (1 - option["risk_probability"])
    )

    print(
        f"{option['name']} "
        f"Safe Utility = {safe_utility}"
    )

    if safe_utility > best_value:

        best_value = safe_utility

        best_option = option["name"]

print("\nSafest Best Decision :", best_option)
