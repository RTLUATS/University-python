karta = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
         "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
         "A": 10, "B": 11, "C": 12, "D": 13,
         "E": 14, "F": 15,
         }

invers_karta = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
                "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}


def func_sum(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    helpstr = ""
    newstr = ""
    for x in range(len(num2)):
        caching_num1 = karta.get(num1[x])
        caching_num2 = karta.get(num2[x])
        caching_helpstr = karta.get(helpstr)
        if (helpstr.isdigit()) and (caching_num1 + caching_num2 + caching_helpstr) >= 16:
            if (caching_num1 + caching_num2 + caching_helpstr) - 16 > 9:
                newstr = newstr + invers_karta.get(str((caching_num1 + caching_num2 + caching_helpstr) - 16))
            else:
                newstr = newstr + str((caching_num1 + caching_num2 + caching_helpstr) - 16)
            helpstr = "1"
        elif (caching_num1 + caching_num2) >= 16:
            if (caching_num1 + caching_num2) - 16 > 9:
                newstr = newstr + invers_karta.get(str((caching_num1 + caching_num2 - 16)))
            else:
                newstr = newstr + str((caching_num1 + caching_num2) - 16)
            helpstr = "1"
        elif helpstr.isdigit():
            if (caching_num1 + caching_num2 + caching_helpstr) > 9:
                newstr = newstr + invers_karta.get(str(caching_num1 + caching_num2 + caching_helpstr))
            else:
                newstr = newstr + str(caching_num1 + caching_num2 + caching_helpstr)
            helpstr = ""
        else:
            if (caching_num1 + caching_num2) > 9:
                newstr = newstr + invers_karta.get(str(caching_num1 + caching_num2))
            else:
                newstr = newstr + str(caching_num1 + caching_num2)
    if len(num1) > len(num2):
        for x in range(len(num1) - len(num2)):
            caching = karta.get(num1[x - (len(num1) - len(num2))])
            if helpstr.isdigit() and (karta.get(helpstr) + caching >= 16):
                if (caching + karta.get(helpstr)) - 16 > 9:
                    newstr = newstr + invers_karta.get(str((caching + karta.get(helpstr)) - 16))
                else:
                    newstr = newstr + str((caching + karta.get(helpstr)) - 16)
                helpstr = "1"
            elif helpstr.isdigit():
                newstr = newstr + invers_karta.get(str(caching + karta.get(helpstr)))
                helpstr = ""
            else:
                newstr = newstr + num1[x - (len(num1) - len(num2))]
    if helpstr.isdigit():
        newstr = newstr + helpstr
    newstr = newstr[::-1]
    return newstr


def func_min(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    num1 = list(num1)
    num2 = list(num2)
    help_list = []
    newstr = ""
    for range_num2 in range(len(num2)):
        caching_num1 = karta.get(num1[range_num2])
        caching_num2 = karta.get(num2[range_num2])
        if help_list:
            newstr = newstr + invers_karta.get(str((caching_num1 + int(help_list[-1])) - caching_num2))
            help_list = help_list.remove(help_list[len(help_list) - 1])
        else:
            if caching_num1 > caching_num2:
                newstr = newstr + invers_karta.get(str(caching_num1 - caching_num2))
            else:
                a = 0
                for x in range(1, len(num1)):
                    if a == 0:
                        caching_num1_2 = num1[range_num2 + x]
                        if caching_num1_2 != "0":
                            num1[range_num2 + x] = invers_karta.get(str(karta.get(caching_num1_2) - 1))
                            a = 1
                        else:
                            help_list.append("15")
                help_list.append("16")
                newstr = newstr + invers_karta.get(
                    str((caching_num1 + int(help_list[len(help_list) - 1])) - caching_num2))
                help_list = help_list.remove(help_list[len(help_list) - 1])
    if len(num1) > len(num2):
        for x in range(len(num1) - len(num2)):
            newstr = newstr + num1[x + len(num2)]
    newstr = newstr[::-1]
    return newstr


if __name__ == '__maine__':
    try:
        num1 = str(input(print("Введите 1-е число для сложения:")))
    except:
        print("Ошибочка молодой человек")
    else:
        if set(num1) <= set("0123456789ABCDEF"):
            try:
                num2 = str(input(print("Введите второе число:")))
            except:
                print("Ошибочка молодой человек")
            else:
                if set(num2) <= set("0123456789ABCDEF"):
                    flag = 1
                    while flag == 1:
                        if (num1[0] == "0"):
                            num1 = num1[1::1]
                        elif (num2[0] == "0"):
                            num2 = num2[1::1]
                        else:
                            flag = 0
                    if len(num1) >= len(num2):
                        print(f'Сложение: {func_sum(num1, num2)}\nВычитание: {func_min(num1, num2)}')
                    else:
                        print(f'Сложение: {func_sum(num2, num1)}\nВычитание: -{func_min(num2, num1)}')
                else:
                    print("число не 16-е")
        else:
            print("число не 16-е")
