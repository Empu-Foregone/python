def calculate_total_distance(n, initial_distance=10, increase_rate=0.1):
    """Calculates the total distance that the athlete will run.

    Args:
        n: number of days.
        initial_distance: Initial distance (default 10 km).
        increase_rate: Daily distance increase factor (default 10%).

    Returns:
        Total distance.
    """

    total_distance = 0
    distance = initial_distance
    for _ in range(n):
        total_distance += distance
        distance *= (1 + increase_rate)
    return total_distance