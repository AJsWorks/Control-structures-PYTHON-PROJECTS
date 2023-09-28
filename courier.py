# Compulsory Task 3

# Asking a customer the price of the item and distance of delivery and change it to float data type.
item_price = float(input("Enter the price of an item you would like to purchase: "))
distance = float(input("Enter the total distance of delivery in KMs: "))

# Listing out the delivery options with respective costs:

air_delivery = 0.36 * distance
freight_delivery = 0.25 * distance
full_insurance = 50
limited_insurance = 25
gift_yes = 15
gift_no = 0
priority_delivery = 100
standard_delivery = 20

# Now ask customer their preferred delivery options to calculate the total cost
delivery_type = input("Please select delivery type(Air or Freight): ").capitalize()
insurance_limit = input("Please select the type of insurance for your item(Full or Limited): ").capitalize()
gift_option = input("Do you want a gift wrap?(Yes/No): ").capitalize()
priority_preference = input("Do you want priority delivery?(Yes/No): ").capitalize()

if delivery_type == "Air":
    total_cost = item_price + air_delivery
else:
    total_cost = item_price + freight_delivery

if insurance_limit == "Full":
    total_cost += full_insurance
else:
    total_cost += limited_insurance

if gift_option == "Yes":
    total_cost += gift_yes
else:
    total_cost += gift_no

if priority_preference == "Yes":
    total_cost += priority_delivery
else:
    total_cost += standard_delivery

print("Total cost of sending the item considering your preferences is: R" + str(total_cost))


