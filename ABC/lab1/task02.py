karta = {"10": "A", "11": "B", "12": "C","13": "D", "14": "E", "15": "F"}

def function(num, calculus):
    calculus = int(calculus)
    flag = 1
    numstr = ""
    num = int(num)
    if calculus == 16:
        while flag == 1:
            if num < calculus:
                flag = 0
                if num > 9:
                    numstr = numstr + karta.get(str(num))
                else:
                    numstr = numstr + (str(num))
                numstr = numstr[::-1]
            else:
                if num % calculus > 9:
                    numstr = numstr + karta.get(str(num % calculus))
                else:
                    numstr = numstr + str(num % calculus)
                num = num // calculus
    else:
        while flag == 1:
            if num < calculus:
                flag = 0
                numstr = numstr + (str(num))
                numstr = numstr[::-1]
            else:
                numstr = numstr + str(num % calculus)
                num = num // calculus
    print("Результат =", numstr)
    return


try:
    num = str(input(print("Введите число:")))
except:
    print("Ошибочка молодой человек")
else:
    if set(num) <= set("0123456789"):
        try:
            calculusSystem = str(input(print("Введите систему исчислений:")))
        except:
            print("Ошибочка молодой человек")
        else:
            if calculusSystem == "2":
                function(num, calculusSystem)
            elif calculusSystem == "8":
                function(num, calculusSystem)
            elif calculusSystem == "16":
                function(num, calculusSystem)
            else:
                print("Ошибочка я такой системы не знаю")
    else:
        print("Это не 10-е число")