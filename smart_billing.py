# Python Project #
# My First Project #



Costomer_Name= input("Enter your name : ")
Costomer_Email= input("Enter your Email : ")
Contact_Number= input("Enter your Contact Number : ")
Product_Name= input("Enter your Product Name : ")
Quantity= int(input("Enter your Quantity : "))
selling_price = float(input("Enter your Selling Price : "))
cost_price_per_Unit= float(input("Enter your Cost Price : "))
discount = float(input("Enter your Discount(%) : "))
gst = float(input("Enter your GST(%) : "))
revenue = selling_price * Quantity
discount_amt = revenue * discount / 100
taxable_amount = revenue - discount_amt
gst_amt = taxable_amount * gst / 100
final_bill = taxable_amount + gst_amt
total_cost = cost_price_per_Unit * Quantity
profit = taxable_amount - total_cost          #Gst goes to government so we will not consider gst in profit calculation
margin = profit / taxable_amount * 100

status = "Profitable" if profit > 0 else "Loss"
high_margin = margin > 20 and profit > 0

print("---------------------------------------------------")
print("---------------------------------------------------")
print(         " RETAIL SALES BILL/ FINAL_BILL")     
print("---------------------------------------------------")
print("---------------------------------------------------")

print("Coustomer Name : ",Costomer_Name.strip().title())
print("Coustomer Email : ",Costomer_Email)
print("Contact Number : ",Contact_Number)
print("---------------------------------------------------")
print("Product Name : ",Product_Name)
print("Product Code : ",Product_Name[0:3].upper().replace(" ","_"))
print("Quantity : ",Quantity)
print("Selling Price Per Unit : ",selling_price)
print("Cost Price Per Unit : ",cost_price_per_Unit)
print("Total Cost : ",total_cost)
print("---------------------------------------------------")

print("Coustomer_ID - ",Costomer_Name[0:3].upper() + "-" + str(Contact_Number)[-4:])
print("Domain : ",Costomer_Email[Costomer_Email.find("@")+1:])
print("Domain End With 'com' : ",Costomer_Email.endswith("com"))

print("---------------------------------------------------")
print(              "Revenue : ",revenue)
print("---------------------------------------------------")
print("Discount Amount : ",discount_amt)
print("Selling Price : ",selling_price)
print("Profit : ",profit)
print("Profit Margin(%) : ",margin)
print("GST Amount : ",gst_amt)
print("Status : ",status)
print("High Margin : ",high_margin)
print("---------------------------------------------------")
print("---------------------------------------------------")
print("Final Bill : ",final_bill)
print("---------------------------------------------------")
print("---------------------------------------------------")



