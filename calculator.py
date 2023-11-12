def calcular(resultado_anterior):
  if resultado_anterior is None:
    num1 = float(input("Insira o primeiro valor: "))
  else:
    num1 = resultado_anterior
  operacao = input("Insira a operação (+, -, *, /, **): ")
  num2 = float(input("Insira o segundo valor: "))

  if operacao == "+":
      resultado = num1 + num2
  elif operacao == "-":
      resultado = num1 - num2
  elif operacao == "*":
      resultado = num1 * num2
  elif operacao == "/":
      resultado = num1 / num2
  elif operacao == "**":
      resultado = num1 ** num2
  else:
      print("Operação inválida")
      calcular(resultado_anterior)

  print(f"O resultado é {resultado}")
  continuar = input("Deseja continuar? (s/n): ")
  if continuar == "s":
      calcular(resultado)
  else:
        print("Programa terminado")
calcular(None)

"""def calcular():
    num1 = float(input("Insira o primeiro valor: "))
    operacao = input("Insira a operação (+, -, *, /, **): ")
    num2 = float(input("Insira o segundo valor: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    elif operacao == "**":
        resultado = num1 ** num2
    else:
        print("Operação inválida")
        calcular()

    print(f"O resultado é {resultado}")
    continuar = input("Deseja continuar? (s/n): ")
    if continuar == "s":
        calcular()
    else:
        print("Programa terminado")

calcular()"""