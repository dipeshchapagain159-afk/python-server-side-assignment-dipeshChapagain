#Parse a JSON file representating product details(name,price,quantity) and display the details in tabular format;
import json

displays=[]
num = int(input("Enter the number of product: "))
for i in range(num):
    display={
        'name':input("Enter name of product: "),
        'price':int(input("Enter the price: ")),
        'quantity':int(input("Enter it's quantity: ")),
    }
    displays.append(display)
with open('visitor.json','w') as file:
    json.dump(display,file,indent=4)
print("Dta has been written")

print(f"{'Name':<15}{'Price':<15}{'Quantity':<15}")
print("-" * 45)
for p in displays:
    print(f"{p['name']:<15}{p['price']:<15}{p['quantity']:<15}")