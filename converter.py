def convert_mile():
    return int(input("Введите колличество миль: ")) * 1.609


def convert_inch():
    return int(input("Введите колличество дюймов: ")) * 25.4


def convert_yard():
    return int(input("Введите колличество ярдов: ")) * 0.9144


if __name__ == '__main__':
    print("Километров в милях: "f"{convert_mile()}")
    print("Милиметров в дюймах: "f"{convert_inch()}")
    print("Метров в ярдах: "f"{convert_inch()}")
