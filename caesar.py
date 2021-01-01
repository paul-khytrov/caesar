b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1",
     "2", "3", "4", "5", "6", "7", "8", "9"]


def caesar(a):
    d = ""
    a = a.upper()
    for i in range(len(a)):
        if a[i] == "X":
            d = d + a[i].replace(a[i], "A")
        elif a[i] == "Y":
            d = d + a[i].replace(a[i], "B")
        elif a[i] == "Z":
            d = d + a[i].replace(a[i], "C")
        elif a[i] == " ":
            d = d + a[i].replace(a[i], " ")
        elif not a[i].isalnum():
            d = d + a[i]
        else:
            if a[i] == "7":
                d = d + "0"
            elif a[i] == "8":
                d = d + "1"
            elif a[i] == "9":
                d = d + "2"
            elif a[i].isnumeric():
                d = d + b[b.index(a[i])+3]
            else:
                d = d + a[i].replace(a[i], b[b.index(a[i])+3])
    print(d)
    return d


def decode(a):
    d = ""
    a = a.upper()
    for i in range(len(a)):
        if a[i] == "A":
            d = d + a[i].replace(a[i], "X")
        elif a[i] == "B":
            d = d + a[i].replace(a[i], "Y")
        elif a[i] == "C":
            d = d + a[i].replace(a[i], "Z")
        elif a[i] == " ":
            d = d + a[i].replace(a[i], " ")
        elif not a[i].isalpha():
            d = d + a[i]
        else:
            if a[i] == "0":
                d = d + "7"
            elif a[i] == "1":
                d = d + "8"
            elif a[i] == "2":
                d = d + "9"
            elif a[i].isnumeric():
                d = d + b[b.index(a[i])-3]
            else:
                d = d + a[i].replace(a[i], b[b.index(a[i])-3])
    return d


caesar(input())
