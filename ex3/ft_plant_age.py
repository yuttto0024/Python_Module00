def ft_plant_age() -> None:
    """
    Takes input of int and determine if it can be harvest
    """
    plant_age = input("Enter plant age in days: ")
    if int(plant_age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
