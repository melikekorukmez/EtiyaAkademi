number1 = int(input("bir sayi giriniz: "))
number2 = int(input("bir sayi giriniz: "))
number3 = int(input("bir sayi giriniz: "))
number4 = int(input("bir sayi giriniz: "))
number5 = int(input("bir sayi giriniz: "))
number6 = int(input("bir sayi giriniz: "))
number7 = int(input("bir sayi giriniz: "))
number8 = int(input("bir sayi giriniz: "))
number9 = int(input("bir sayi giriniz: "))
number10 = int(input("bir sayi giriniz: "))


numbers = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10]

max = 0
for number in numbers:
    if number > max:
        max = number
print(max)


for i in range(0,max,2):
    print(i)

min = max
for number in numbers:
    if number < min:
        min = number
print(min)

print(max(numbers))



