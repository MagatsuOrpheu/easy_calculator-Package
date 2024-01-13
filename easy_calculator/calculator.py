menu = """
======= (X| Operation |Y) =======
[1]\tSoma             
[2]\tSubtração        
[3]\tMultiplicação    
[4]\tDivisão          
[0]\tSair
=>"""


def main():
  while True:
    opção = str(input(menu))
    print('=================================')

    if opção == '1':
      x, y = numbers()
      soma(x, y)

    elif opção == '2':
      x, y = numbers()
      subtracao(x, y)

    elif opção == '3':
      x, y = numbers()
      multiplicacao(x, y)

    elif opção == '4':
      x, y = numbers()
      divisao(x, y)

    else:
      print("Obrigado por usar a calculadora =)")
      break


def soma(x, y):
  try:
    res = x + y
    print(f"{x} + {y} = {res}")
    print("============== FIM ==============")
  except ValueError:
    print("Digite apenas valores válidos.")


def subtracao(x, y):
  try:
    res = x - y
    print(f"{x} - {y} = {res}")
    print("============== FIM ==============")
  except ValueError:
    print("Digite apenas valores válidos.")


def multiplicacao(x, y):
  try:
    res = x * y
    print(f"{x} X {y} = {res}")
    print("============== FIM ==============")
  except ValueError:
    print("Digite apenas valores válidos.")


def divisao(x, y):
  try:
    res = x / y
    print(f"{x} / {y} = {res:.2f}")
    print("============== FIM ==============")
  except ValueError:
    print("Digite apenas valores válidos.")


def numbers():
  x = int(input("Por favor digite X: "))
  y = int(input("Por favor digite Y: "))
  return x, y


if __name__ == '__main__':
    main()