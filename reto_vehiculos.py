def clasificar_vehiculo():
  numero_ruedas = int(input("Número de ruedas del vehículo: "))
  tipo_combustible = input("Tipo de combustible (diesel, eléctrico o gasolina): ")
  emision_co2 =  float(input("tipo de emisión (g/km): "))

  if numero_ruedas == 2:
      if tipo_combustible == "gasolina" and emision_co2 < 150:
          print("Es una moto contaminante")
      elif tipo_combustible == "eléctrico":
          print("Es una moto eléctrica")
      else:
          print("Es una moto convencional")
        
  elif numero_ruedas == 4:
if tipo_combustible == "eléctrico":
  print("Es un coche eléctrico")
else:
 print("Es un vehículo convencional")
clasificar_vehiculo()


  
