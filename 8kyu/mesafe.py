def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump==mpg*fuel_left:
        return True
    return False

zero_fuel(50, 25, 2)
        

