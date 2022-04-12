def main():
    menu = {
        'mile': mile_milli,
        'inch': inch_milli,
        'yard': yard_milli
    }
    while True:
        cmd = input("Выберите единицы измерения для перевода"
                    f" из {list(menu.keys())}: ")
        if cmd in menu.keys():
            menu[cmd]()


def out(inp, milli, units):
    menu = {
        'milli': [None, 'миллиметров'],
        'centi': [milli_centi, 'сантиметров'],
        'deci': [milli_deci, 'дециметров'],
        'meter': [milli_meter, 'метров'],
        'kilo': [milli_kilo, 'километров']
    }
    while True:
        cmd = input("Выберите единицы измерения для отображения"
                    f" из {list(menu.keys())}: ")
        if cmd == 'milli':
            answer = [milli, menu[cmd][1]]
            break
        if cmd in menu.keys():
            answer = [menu[cmd][0](milli), menu[cmd][1]]
            break
    print(f'{inp} {units} = {answer[0]} {answer[1]}')


def milli_centi(milli):
    return milli / 10


def milli_deci(milli):
    return milli / 100


def milli_meter(milli):
    return milli / 1000


def milli_kilo(milli):
    return milli / 1000000


def mile_milli():
    inp = float(input("Введите колличество миль: "))
    milli = inp * 1609000
    out(inp, milli, 'миль')


def inch_milli():
    inp = float(input("Введите колличество дюймов: "))
    milli = inp * 25.4
    out(inp, milli, 'дюймов')


def yard_milli():
    inp = float(input("Введите колличество ярдов: "))
    milli = inp * 914.4
    out(inp, milli, 'ярдов')


if __name__ == '__main__':
    main()
