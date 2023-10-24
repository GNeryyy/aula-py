def calculadora(operador, numero1, numero2):
  
  if operador == "+":
    return numero1 + numero2
  elif operador == "-":
    return numero1 - numero2
  elif operador == "/":
    return numero1 / numero2
  elif operador == "x":
    return numero1 * numero2
  else:
    raise ValueError("Operador inválido.")


def main():
 
  operador = input("Digite o operador: ")
  numero1 = float(input("Digite o primeiro número: "))
  numero2 = float(input("Digite o segundo número: "))

  resultado = calculadora(operador, numero1, numero2)
  print(f"O resultado é {resultado}")


if __name__ == "__main__":
  main()
