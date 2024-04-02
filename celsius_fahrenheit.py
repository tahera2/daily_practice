# Hi everyone! 
# Here we are going to change the 2 parameters of tempreture (Celsius and Fahrenhiet)
# First ask the user to which value they want to change it: celsius or fahrenheit
# than acoording to thier choice we will do some math operation and print the result for them with 2 float value.
# Try it yourself, then compare to mine one, Maybe you code it in more easy way :).  


choice = input("For changing the degree to celsius write 'c', for changing to fahrenheit wrirte 'f' : ").lower()

if choice == "c":
        celsius = float ( input("Enter the celsius value to change it in fahrenheit :  "))
        fahrenheit_celsius = (celsius * (1.8)) +32
        print(f"{celsius:.2f} C is equal to {fahrenheit_celsius:.2f} F.")
else:
        fahrenheit = float ( input("Enter the fahrenheit value to change it in celsius :  "))
        celsius_fahrenheit = ((fahrenheit - 32)/1.8) 
        print(f"{fahrenheit:.2f} F is equal to {celsius_fahrenheit:.2f} C.")