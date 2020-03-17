karta = {"A": 10, "a": 10, "B": 11, "b": 11, "C": 12, "c": 12,
         "D": 13, "d": 13, "E": 14, "e": 14, "F": 15, "f": 15}
try:
    calculusSystem = str(input(print("Введите систему исчисления:")))
except:
    print("Ошибочка молодой человек")
else:
    if calculusSystem == "16":
        try:
            num = str(input(print("Введите число:")))
        except:
            print("Ошибочка молодой человек")
        else:
            if set(num) <= set("0123456789abcdefABCDEF"):
                count = len(num) - 1
                result = 0
                for x in num:
                    if karta.get(x) is None:
                        result = result + int(x) * 16 ** count
                        count = count - 1
                    else:
                        result = result + int(karta.get(x)) * 16 ** count
                        count = count - 1
                print("Результат =", result)
            else:
                print("Не 16-ое")
    else:
        print("Не правильная система исчисления")