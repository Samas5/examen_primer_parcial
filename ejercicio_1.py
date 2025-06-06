def impresion_pares(n):
	if not n.isdigit():
		raise ValueError("Debes introducir un número entero")
	num = int(n)
	if num < 200 or num > 400:
		raise ValueError("Debe ser un número entre 200 y 400")
	if not num % 2 == 0:
		raise ValueError("El número debe ser par")
	
	lista = []
	for i in range (num, 400 + 1):
		if i % 2 == 0:
			lista.append(i)
		i += 1
	return lista
	
while True:
	try:
		num = input("Introduce un número entre 200 y 400: ")
		print(impresion_pares(num))
	except ValueError as e:
		print(f"Error: {e}")
	salida = input("Ingresa 0 para salir, cualquier otro valor para continuar: ")
	if salida == "0":
		break
print("----------FIN DEL PROGRAMA----------")
		 
	
	
