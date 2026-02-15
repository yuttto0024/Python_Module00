def _countdown_recursive(deadline: int, current_days: int) -> None:
    """
    Perform the recursive countdown for Harvest days
    """
    if current_days > deadline:
        return
    print(f"Day {current_days}")
    _countdown_recursive(deadline, current_days + 1)


def ft_count_harvest_recursive() -> None:
    """
    Caluculate the remaining days until harvest days by a recursive approach
    """
    remaining_days = input("Days until harvest: ")
    _countdown_recursive(int(remaining_days), 1)
    print("Harvest time!")
