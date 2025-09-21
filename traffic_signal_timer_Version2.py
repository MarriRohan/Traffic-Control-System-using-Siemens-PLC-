def allocate_green_time(traffic_densities, total_cycle_time=120, min_green_time=10):
    """
    Allocates green time for each lane based on traffic density.

    Args:
        traffic_densities (list of int/float): Traffic density for each lane.
        total_cycle_time (int): Total time for one complete cycle (in seconds).
        min_green_time (int): Minimum green time for each lane (in seconds).

    Returns:
        list of int: Allocated green time for each lane.
    """
    n_lanes = len(traffic_densities)
    # Ensure at least min_green_time for each lane
    time_remaining = total_cycle_time - n_lanes * min_green_time
    total_density = sum(traffic_densities)
    green_times = []

    for density in traffic_densities:
        if total_density == 0:
            # If no traffic, allocate minimum time
            green_times.append(min_green_time)
        else:
            # Proportional allocation
            time_for_lane = min_green_time + int((density / total_density) * time_remaining)
            green_times.append(time_for_lane)

    # Adjustment: ensure total does not exceed total_cycle_time
    total_allocated = sum(green_times)
    if total_allocated > total_cycle_time:
        # Reduce excess from the lane with the most time
        max_idx = green_times.index(max(green_times))
        green_times[max_idx] -= (total_allocated - total_cycle_time)
    elif total_allocated < total_cycle_time:
        # Add remaining time to the lane with the most traffic
        max_idx = traffic_densities.index(max(traffic_densities))
        green_times[max_idx] += (total_cycle_time - total_allocated)

    return green_times

# Example usage:
if __name__ == "__main__":
    traffic_densities = [10, 30, 20, 40]  # Example densities for 4 lanes
    green_times = allocate_green_time(traffic_densities)
    for i, t in enumerate(green_times):
        print(f"Lane {i+1}: {t} seconds green")