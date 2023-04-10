
def toplama():
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    print(number1, "+", number2, "=", number1+number2) 

def cikarma():
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    print(number1, "-", number2, "=", number1-number2) 

def carpma():
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    print(number1, "*", number2, "=", number1*number2) 

def bolme():
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    print(number1, "/", number2, "=", number1/number2) 

def modAlma():
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    print(number1, "%", number2, "=", number1%number2) 

while (1):
    secim = input("seciminiz (+ ,-,*,/,% ,q):")
    if secim=="q":
        break
    number1 = int(input("sayi giriniz"))
    number2 = int(input("sayi giriniz"))
    if secim == "+":
        print(number1, "+", number2, "=", number1+number2) 
    elif secim == "-":
       print(number1, "-", number2, "=", number1-number2)
    elif secim == "*":
       print(number1, "*", number2, "=", number1*number2) 
    elif secim == "/":
        print(number1, "/", number2, "=", number1/number2)
    elif secim == "%":
      print(number1, "%", number2, "=", number1%number2)
    else:
        print("geçersiz")  