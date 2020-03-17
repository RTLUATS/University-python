karta = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
         "0100": "4", "0101": "5", "0110": "6", "0111": "7",
         "1000": "8", "1001": "9", "1010": "A", "1011": "B",
         "1100": "C", "1101": "D", "1110": "E", "1111": "F"}

def func(strin):
    newstr = ""
    str_list = []
    for i in range(0, len(strin), 4):
        str_list.append(strin[i:i + 4])
    for x in str_list:
        newstr = newstr + str(karta.get(x))
    print("В 16-ой: " + newstr + "\nВ 2-й: " + strin)
    return


try:
    binary = str(input("Введите строку из 0 и 1:"))
except:
    print("Ошибочка")
else:
    if set(binary) <= set("01"):
        if len(binary) % 4 != 0:
            if (len(binary) + 1) % 4 == 0:
                newstr = "0" + binary
                func(newstr)
            elif (len(binary) + 2) % 4 == 0:
                newstr = "00" + binary
                func(newstr)
            elif (len(binary) + 3) % 4 == 0:
                newstr = "000" + binary
                func(newstr)
        else:
            func(binary)
    else:
        print("А число-то не двоичное!")