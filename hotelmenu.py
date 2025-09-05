menu ={
    'pizza': 120,
    'coffee': 50,
    'icecream': 30,
    'burger': 80
}
print("welcome to PRIYANKA Resturent")
print("pizz : 120\ncoffee : 50\nicecream : 30\nburger : 80")
order_total = 0
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f" Your item {item_1} has been added to your order ")
else:
    print(f"your item{item_1} is not avaialable yet! ")   
another_order = input("do you want to add anothe item ? (yes/no)")
if another_order =="yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"item{item_2} has been added to order")
    else:
        print(f"ordered item{item_2} is not avaiable!") 
print(f"the total amount of item to pay is {order_total}")   
print("Thank you for ordering")            