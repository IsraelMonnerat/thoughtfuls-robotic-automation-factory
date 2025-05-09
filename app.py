

def sort(width: float, height: float, length: float, mass: float) -> str:
    """Determines the shipping category of a package based on its dimensions and weight.

    Dimensions are checked against a threshold for bulkiness, and weight is checked
    against a threshold for heaviness. If both thresholds are met, the package is
    rejected. If either threshold is met, the package is marked as special. If neither
    threshold is met, the package is marked as standard.

    Parameters:
        width (float): the width of the package in cm
        height (float): the height of the package in cm
        length (float): the length of the package in cm
        mass (float): the mass of the package in kg

    Returns:
        str: the shipping category of the package, one of "REJECTED", "SPECIAL", or "STANDARD"
    """
    is_bulky = check_bulky(width, height, length)
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def check_bulky(width: float, height: float, length: float) -> bool:
    """
        Check if package is bulky based on dimensions and volume.
    """
    dimensions = [width, height, length]
    for dim in dimensions:
        if dim >= 150:
            return True
    
    volume = width * height * length
    if volume >=  1_000_000:
        return True
    
    return False


if __name__ == '__main__':
    try:
        width = float(input("Enter the width of the package in cm: "))
        height = float(input("Enter the height of the package in cm: "))
        length = float(input("Enter the length of the package in cm: "))
        mass = float(input("Enter the mass of the package in kg: "))
    except ValueError:
        print("Please, enter valid numbers.")
        exit(1)
    result = sort(width, height, length, mass)
    print(result)
