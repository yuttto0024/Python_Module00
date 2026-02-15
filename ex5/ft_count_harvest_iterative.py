def ft_count_harvest_iterative() -> None:
    """
    Calculate the remaining days until harvest days by an iterative approach
    """
    remaining_days = input("Days until harvest: ")
    for i in range(1, int(remaining_days) + 1):
        print(f"Day {i}")
    print("Harvest time!")
