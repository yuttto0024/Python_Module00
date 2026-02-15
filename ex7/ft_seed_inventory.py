def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Display the seed inventory details based on the measurement unit
    """
    formatted_name = seed_type.capitalize()
    if unit == "packets":
        print(f"{formatted_name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{formatted_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{formatted_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
