def ft_count_harvest_iterative() -> None:
    """
    Calculate the remaining days until harvest days by an iterative approach
    """
    remaining_days = input("Days until harvest: ")
    for i in range(int(remaining_days)):
        print(f"Day {i}")
    print("Harvest time!")
