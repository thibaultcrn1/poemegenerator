import random

print("-------------------------")
print("-- Générateur de poème --")
print("-------------------------")
print("")

response = float(input("Quel type de phrase ? Syntaxe: 4444 ou 4433 "))
print()

list = [
  "test1",
  "test2",
  "test3",
  "test4"
]

if response == 4444:
  print('\n'.join(random.sample(list, 4)))
  print()
  print('\n'.join(random.sample(list, 4)))
  print()
  print('\n'.join(random.sample(list, 4)))
  print()
  print('\n'.join(random.sample(list, 4)))
  
if response == 4433:
  print('\n'.join(random.sample(list, 4)))
  print()
  print('\n'.join(random.sample(list, 4)))
  print()
  print('\n'.join(random.sample(list, 3)))
  print()
  print('\n'.join(random.sample(list, 3)))
  print()
