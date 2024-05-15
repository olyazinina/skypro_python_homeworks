def bank(x, y):
    for n in range(y):
        x += (x / 10)
    return(x)
x = int(input("Введите сумму вклада: "))
y = int(input("Срок (лет): "))
result = bank(x, y)
print("Сумма на счёте за", y, "лет составляет", result, "руб.")