import copy


def flip(coin):
    """[summary]
    Flips the coins.
    Args:
        coin ([int]): Can be either 0 (heads) or 1 (tails)

    Returns:
        [int]: 0 if input was 1 and 1 if input was 0
    """
    if coin == 0:
        return 1
    elif coin == 1:
        return 0


def count_flips(coins, starting_value):
    """[summary]
    Helper function to get number of filps depending on starting value:
    Args:
        coins (List[int]): List of coins 
        starting_value (int): 0 | 1

    Returns:
        [int]: Number of flips for the coins to alternating 0 & 1 and starting with the given starting value. 
    """
    flip_count = 0
    expected_coin = starting_value
    for index, coin in enumerate(coins):
        if not coin == expected_coin:
            coins[index] = flip((coin))
            flip_count += 1
        expected_coin = flip(expected_coin)
    return flip_count


def solution(A):
    """[summary]
    Given an Array of integersrepresenting coins count minimum number of coins needed to be flipped
    for the array to alternating zeros and ones or ones and zeros
    Args:
        A ([list]): Array of coins

    Returns:
        [int]: Minimum number of coins needed to be flipped.
    """
    # Make a copy of A for use in the second iteration
    original_order = copy.deepcopy(A)
    # Count flips when starting with zero and one
    start_with_zero = count_flips(A, 0)
    start_with_one = count_flips(original_order, 1)
    return min(start_with_zero, start_with_one)
