import math

# ==========================================================
# GAME TREE
# ==========================================================

game_tree = {

    "A": ["B", "C"],

    "B": ["D", "E"],

    "C": ["F", "G"],

    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}


# ==========================================================
# MINIMAX
# ==========================================================

def minimax(node, depth, maximizing_player):

    if isinstance(game_tree[node], int):

        return game_tree[node]

    if maximizing_player:

        best_value = -math.inf

        for child in game_tree[node]:

            value = minimax(
                child,
                depth + 1,
                False
            )

            best_value = max(best_value, value)

        return best_value

    else:

        best_value = math.inf

        for child in game_tree[node]:

            value = minimax(
                child,
                depth + 1,
                True
            )

            best_value = min(best_value, value)

        return best_value


# ==========================================================
# ALPHA BETA PRUNING
# ==========================================================

def alpha_beta(node, depth, alpha, beta, maximizing):

    if isinstance(game_tree[node], int):

        return game_tree[node]

    if maximizing:

        value = -math.inf

        for child in game_tree[node]:

            value = max(
                value,
                alpha_beta(
                    child,
                    depth + 1,
                    alpha,
                    beta,
                    False
                )
            )

            alpha = max(alpha, value)

            print(
                f"MAX Node {node} "
                f"Alpha = {alpha}"
            )

            if alpha >= beta:

                print("Pruning Occurred")

                break

        return value

    else:

        value = math.inf

        for child in game_tree[node]:

            value = min(
                value,
                alpha_beta(
                    child,
                    depth + 1,
                    alpha,
                    beta,
                    True
                )
            )

            beta = min(beta, value)

            print(
                f"MIN Node {node} "
                f"Beta = {beta}"
            )

            if alpha >= beta:

                print("Pruning Occurred")

                break

        return value


# ==========================================================
# EXECUTION
# ==========================================================

print("\n========== MINIMAX ==========")

result1 = minimax("A", 0, True)

print("Best Utility :", result1)

print("\n========== ALPHA BETA ==========")

result2 = alpha_beta(
    "A",
    0,
    -math.inf,
    math.inf,
    True
)

print("Optimal Value :", result2)
