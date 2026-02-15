def ft_harvest_total() -> None:
    """
    Takes input of int and displays harvest
    """
    day1 = input("Day1 harvest: ")
    day2 = input("Day2 harvest: ")
    day3 = input("Day3 harvest: ")
    total = int(day1) + int(day2) + int(day3)
    print(f"Total harvest: {total}")
