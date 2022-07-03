import re
from colors import Colors

print(f"{ f'{Colors.yellow}*{Colors.reset}' * 26}\n Indentificador de Vogais \n{f'{Colors.yellow}*{Colors.reset}' * 26}")

vogal = ["a","e","i","o","u"]

while True:
  palavra = input(f"{Colors.green}Digite uma palavra{Colors.reset}: ")
  if palavra == "sair":
    break
  print()
  print(f"{Colors.blue}{palavra} tem {len(palavra)} letras{Colors.reset}")

  """Conta quantas vezes uma vogal se repete dentro da palavra"""
  
  conta = palavra.lower()
  resultado = {}
  for i in vogal:
      if i in palavra:
          resultado[i] = palavra.count(i)
  print(resultado)
  
  """
  Com base na nossa lista conseguimos conferir se as letras dentro 
  da palavra são vogais ou não, caso exista alguma letra com ascento ou números, usamos
  a biblioteca 're' para identificar  esses caracteres.
  """
  for l in palavra.lower():
    if l in vogal:
      print(f"{Colors.yellow}{l.upper()}{Colors.reset} é uma vogal")
    elif re.search('[0-9]', l):
      print(f'{Colors.yellow}{l.upper()}{Colors.reset} isso é um numero')
    elif re.search('Ç|ç', l):
      print(f'{Colors.yellow}{l.upper()}{Colors.reset} é uma consoante')
    elif re.search('[^A-z]', l):
      print(f'{Colors.yellow}{l.upper()}{Colors.reset} é uma vogal')
    else:
      print(f"{Colors.yellow}{l.upper()}{Colors.reset} é uma consoante")