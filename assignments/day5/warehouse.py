inventory=[]

for i in range(3):
    category=input("Enter Category Name:")
    products=[]

    for j in range(3):
        product = input("Enter Product Name:")
        quantity = int(input("Enter Product Quantity:"))
        products.append([product,quantity])
    inventory.append([category,products])

print("\nInventory Report")
for category in inventory:
    print("\nCategory:",category[0])
    
    for product in category: 
        print(f"Product:",products[0],"Quantity:",products[1])