
def toplama():
    print(number1, "+", number2, "=", number1+number2) 

def cikarma():
    print(number1, "-", number2, "=", number1-number2) 

def carpma():
    print(number1, "*", number2, "=", number1*number2) 

def bolme():
    print(number1, "/", number2, "=", number1/number2) 

def modAlma():
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