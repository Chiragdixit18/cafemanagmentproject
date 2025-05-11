x = input("HI would you like to have the menu?")
if x == "yes" or x == "YES" or x == "Yes":
    print("coffee : $60\nburger : $70\ntea : $20")
elif x=="NO" or x== "No" or x == "no":
    print("OKAY thanks for coming!")
else:
    print("I can't understand ")
z={"c":60,"b": 70,"t": 20}
bill = 0
y = input("would you like to order something?")
if y == "Coffee" or y =="coffee":
    print("Sure")
    bill = bill + z["c"]
elif y == "Burger" or y == "burger":
    print("Sure")
    bill = bill + z["b"]
elif y == "Tea" or y == "tea":
    print("Sure")
    bill = bill + z["t"]
else:
    print("not available currently")
for i in range(1,100):
    A = input("do you want something else?")
    if A == "yes" or A == "YES":
        B = input("Tell me please!")
        if B == "Coffee" or B =="coffee":
            print("Sure")
            bill = bill + z["c"]
        elif B == "Burger" or B == "burger":
            print("Sure")
            bill = bill + z["b"]
        elif B == "Tea" or B == "tea":
            print("Sure")
            bill = bill + z["t"]
    else:
        break
print(f"Here is your bill{bill}")
print("Thank you for visiting us")