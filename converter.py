def main():
    menu = {
        'mile': convert_mile,
        'inch': convert_inch,
        'yard': convert_yard
    }
    while True:
        cmd = input(f"Выберите единицы измерения для перевода из {list(menu.keys())}: ")
        if cmd in menu.keys():
            print(menu[cmd]())


def convert_mile():
    return int(input("Введите колличество миль: ")) * 1.609


def convert_inch():
    return int(input("Введите колличество дюймов: ")) * 25.4


def convert_yard():
    return int(input("Введите колличество ярдов: ")) * 0.9144


if __name__ == '__main__':
    main()
