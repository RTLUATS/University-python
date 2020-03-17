karta = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
         "4": "0100", "5": "0101", "0110": "6", "0111": "7"}
try:
    octal = str(input("Введите восьмиричное число: "))
except:
    print("Ошибочка")
else:
    if set(octal) <= set("01234567"):
        binary = ""
        for x in octal:
            binary = binary + karta.get(x)
        print(binary)
    else:
        print("A число-то не восьмиричное")