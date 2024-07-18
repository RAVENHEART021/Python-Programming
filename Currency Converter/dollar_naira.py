#Converter of Dollar to Naira Only

#Take user's input
#input function to take user input
amount = input("Enter amount: $")

#convert the amount input data to float
amount_type_convert = float(amount)

#conversion rate for Dollar to Naira
rate = 1400
 
def multiply():
    return amount_type_convert * rate

print("your Naira is", multiply())
print()
print("This application only convert $ to #")