print(f"{'*' * 26}\n Indentificador de Vogais \n{'*' * 26}")

vogal = ["a","e","i","o","u"]

while True:
  palavra = input("Digite uma palavra: ")
  if palavra == "sair":
    break
  print()

  print(f"{palavra} tem {len(palavra)} letras")
  conta = palavra.lower()
  resultado = {}

  for i in vogal:
      if i in palavra:
          resultado[i] = palavra.count(i)
  print(resultado)
  
  for l in palavra.lower():
    if l in vogal:
      print(f"{l} é uma vogal")
    else:
      print(f"{l} é uma consoante")
