# basic calculator 

operator = input("yapmak istediğiniz işlemi seçiniz. (+ - / * )")
num1= float(input("1. sayıyı giriniz: "))
num2= float(input("2. sayıyı giriniz: "))

if operator == "+":
    result = num1 +num2 
    print(round(result ,3 ))
elif operator == "-" :
    result = num1-num2 
    print(round(result ,3 ))
elif operator == "/" :
    result = num1/num2 
    print(round(result ,3 ))
elif operator =="*" :
    result = num1*num2
    print(round(result ,3 ))
else :
    print("yanlış işlemi yazdınız.")
