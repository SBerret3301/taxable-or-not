n = int(input("enter your age : "))
s = input("enter your gender : ")
while n <= 0  :
    n = int(input("enter corectly your age : "))
while (s != "male" and s != "female") :
    s = input("enter corectly your gender : ")
if n > 20 and s == "male" :
    print("you are taxable")
elif (n >= 18 and n <= 35) and s == "female" :
    print("you are taxable")
else :
    print("you aren't taxable")
