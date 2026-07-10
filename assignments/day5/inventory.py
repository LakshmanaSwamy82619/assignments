products = ["Laptop","Mouse","Keyboard"]

print("Initial Inventory")
print(products)

products.append("Monitor")
print("After adding Some Urgent Products")
print(products)

new_products = ["Tablet","Webcam"]
products.extend(new_products)
print("After Combining the products from another warehouse")
print(products)

products.remove("Mouse")
print("After remoing the disconnected products")
print(products)

shipped_one = products.pop()
print("Shipped Product:",shipped_one)
print("After Shipping Inventory",products)

print("Laptop Appears:",products.count("Laptop")," times")
print("Finding the Monitor Index:",products.index("Monitor"))

products.sort()
print("After sorting the products")
print(products)

products.reverse()
print("After reversing the order")
print(products)

temp = products.copy()
print("Backup COpy of Products")
print(products)

temp_invent = products.copy()
temp_invent.clear()
print("Temporary Inventory List:")
print(temp_invent)