def descomponer_palabra(palabra):
	if palabra == "" or palabra == " ":
		raise ValueError("La palabra no puede estar vacía")
	if not palabra.isalpha():
		raise ValueError("Deben ser carácteres, sin espacios")
	lista = []
	for letra in palabra:
		lista.append(letra)
	return lista
	
while True:
	try:
		palabra = input("Ingresa una palabra: ")
		letras = descomponer_palabra(palabra)
		contador = 1
		for letra in letras:
			print(f"Letra {contador}: {letra}")
			contador += 1
	except ValueError as e:
		print(f"Error {e}")
	salida = input("Ingresa 0 para salir, cualquier otro valor para continuar: ")
	if salida == "0":
		break
print("----------FIN DEL PROGRAMA----------")
	
