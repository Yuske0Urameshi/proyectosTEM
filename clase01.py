print ("hOLA MUNDO desde python")
#variables numericos 
edad = 25 #Entero
altura = 1.75 #flotante
bandera = True #booleano
nombre = "Bruno Diaz" #String
print("\nPrint tradicional")

print("mi nombre es: ", nombre)
print("mi edad es: ", edad)
print("mi altura es: ", altura)
print("mi color es: ", bandera)
print("-------------------")




#Entrada de datos
print("\nEntrada de datos")
print("-------------------")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu Edad: "))
altura = float(input("Ingresa tu altura: "))
bandera = input("Estas vivo? (True/False): ")

print("\nPrint moderno")
#segunda forma de imprimir
print()
print(f"Mi nombre es:  {nombre}")
print(f"mi edad es: {edad}")
print(f"mi altura es: {altura}")
print(f"mi color es: {bandera}")