def ft_water_reminder() -> None:
    """
    Determine whether we have to water or not
    """
    since_day = input("Days since last watering: ")
    if int(since_day) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
