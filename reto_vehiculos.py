numero_ruedas = int(input("Número de ruedas: "))
tipo_combustible = input("Tipo de combustible (gasolina, diésel, eléctrico): ")
emisiones_co2 = float(input("Emisiones de CO2 en g/km: "))

if numero_ruedas == 4 and tipo_combustible == "eléctrico":
    clasificacion = "Vehículo eléctrico"
elif numero_ruedas > 4 and tipo_combustible == "gasolina" and emisiones_co2 > 150:
    clasificacion = "Vehículo grande y contaminante"
else:
    clasificacion = tipo_combustible

  
