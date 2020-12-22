# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def calculate_velocity(measurements):
    """Calculates the velocity based on measurements

    Args:
        measurements list[int]: List of measurements

    Returns:
        list[int]: return list of calculated velocity
    """
    velocity_list = list()
    for i in range(len(measurements)-1):
        velocity_list.append(measurements[i+1] - measurements[i])
    return velocity_list


def solution(A):
    # Set to keep track of results
    results = set()

    # Get list of velocity
    velocity_measurements = calculate_velocity(A)

    # Loop through and loop for area of consistent velocity
    for current_pos in range(len(velocity_measurements)-1):
        for end in range(current_pos+1, len(velocity_measurements)):
            if velocity_measurements[current_pos] == velocity_measurements[end]:
                results.add((current_pos, end))
            else:
                break
    return len(results)
