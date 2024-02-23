#Receives temp. in celsius when water begins to boil
temp_celsius = int(input(""))

#Calculates the atmospheric pressure
atm_pressure = 5 * temp_celsius - 400

#Outputs the atmospheric pressure in kPa
print(str(atm_pressure))