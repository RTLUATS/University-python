from Lab01.task041 import *


def delete_nulls(key, num):
    if key == 1:
        num = num[2::1]
        num = "-" + num
    else:
        num = num[1::1]
    return num


def mult():
    try:
        num1 = str(input(print("Введите 1-е число для умножения:")))
    except:
        print("Ошибочка молодой человек")
    else:
        if set(num1) <= set("0123456789ABCDEF"):
            try:
                num2 = str(input(print("Введите второе число для умножения:")))
            except:
                print("Ошибочка")
            else:
                if set(num2) <= set("0123456789ABCDEF"):
                    flag = 1
                    result = ""
                    while flag == 1:
                        if num1[0] == "0":
                            num1 = delete_nulls(2, num1)
                        elif num2[0] == "0":
                            num2 = delete_nulls(2, num2)
                        elif num1[0] == "-" and num1[1] == "0":
                            num1 = delete_nulls(1, num1)
                        elif num2[0] == "-" and num2[1] == "0":
                            num2 = delete_nulls(2, num2)
                        else:
                            flag = 0
                    if len(num1) >= len(num2):
                        steps = 0
                        count = len(num2) - 1
                        for x in num2:
                            steps = steps + int(karta.get(x)) * 16 ** count
                            count = count - 1
                        for x in range(steps):
                            if len(result) < len(num1):
                                result = func_sum(num1, result)
                            else:
                                result = func_sum(result, num1)
                    else:
                        steps = 0
                        count = len(num1) - 1
                        for x in num1:
                            steps = steps + int(karta.get(x)) * 16 ** count
                            count = count - 1
                        for x in range(steps):
                            if len(result) < len(num2):
                                result = func_sum(num2, result)
                            else:
                                result = func_sum(result, num2)
                    print(f"Умножение : {result}")
    return


def translate_to_hex(num):
    flag = 1
    numstr = ""
    while flag == 1:
        if num < 16:
            flag = 0
            if num > 9:
                numstr = numstr + karta.get(str(num))
            else:
                numstr = numstr + (str(num))
            numstr = numstr[::-1]
        else:
            numstr = numstr + str(karta.get(str(num % 16)))
            num = num // 16
    return numstr


def division():
    try:
        num1 = str(input(print("Введите 1-е число для деления:")))
    except:
        print("Ошибочка молодой человек")
    else:
        if set(num1) <= set("0123456789ABCDEF"):
            try:
                num2 = str(input(print("Введите второе число для деления:")))
            except:
                print("Ошибочка")
            else:
                if set(num2) <= set("0123456789ABCDEF"):
                    flag = 1
                    result = ""
                    while flag == 1:
                        if num1[0] == "0":
                            num1 = delete_nulls(2, num1)
                        elif num2[0] == "0":
                            num2 = delete_nulls(2, num2)
                        elif num1[0] == "-" and num1[1] == "0":
                            num1 = delete_nulls(1, num1)
                        elif num2[0] == "-" and num2[1] == "0":
                            num2 = delete_nulls(2, num2)
                        else:
                            flag = 0
                    result_division = 0
                    count = len(num2) - 1
                    while result != num1:
                        if len(result) < len(num2):
                            result = func_sum(num2, result)
                        else:
                            result = func_sum(result, num2)
                        result_division += 1
                    result_division = translate_to_hex(result_division)
                    print(f"Деление : {result_division}")
    return


mult()
division()
