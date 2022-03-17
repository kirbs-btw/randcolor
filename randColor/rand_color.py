import random

def intToHex(num):
    """
    generates Hex Value form numbers between
    0 - 255
    :return:
    """
    row = '0123456789abcdef'
    countFirst = num // 16
    rest = num - countFirst*16
    hexNum = f"{row[countFirst]}{row[rest]}"
    return hexNum

def randColor():
    """
    generates a random color
    :return: hex value of a random color
    """

    color = f"#{intToHex(random.randint(0, 255))}{intToHex(random.randint(0, 255))}{intToHex(random.randint(0, 255))}"
    return color