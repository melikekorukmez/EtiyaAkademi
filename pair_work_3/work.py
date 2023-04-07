#FIBONACCI SERISI

fib =[1,1]
for i in range(18):
    toplam = fib[i] + fib[i+1]
    fib.append(toplam)
    
print(fib)


#MUKEMMEL SAYI BULMA 

number = int(input("Bir sayi giriniz"))
list = []
toplam = 0 - (number)

for i in range(1,number+1):
    if number % i == 0:
        list.append(i)
        toplam += i

if number == toplam:
    print("MUKEMMELSAYIDIR")
else:
    print("MUKEMMEL SAYI DEGILDIR")